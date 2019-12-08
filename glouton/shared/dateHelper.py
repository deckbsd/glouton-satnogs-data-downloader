import datetime
import calendar


def diff_days(d1, d2):
    return (d1-d2).days*-1


def date_delta(start_date, end_date, no_of_ranges):
    start_epoch = calendar.timegm(start_date.timetuple())
    end_epoch = calendar.timegm(end_date.timetuple())
    date_diff = end_epoch - start_epoch
    step = date_diff / no_of_ranges
    return datetime.timedelta(seconds=step)


def date_span(start_date, end_date, delta=datetime.timedelta(days=1)):
    currentdate = start_date
    first = True
    while currentdate + delta < end_date:
        todate = (currentdate + delta).replace(hour=23, minute=59, second=59)
        if first:
            yield currentdate, todate
            first = False
        else:
            current = currentdate + datetime.timedelta(days=1)
            yield current.replace(hour=0, minute=0, second=0), todate

        currentdate += delta

    todate = todate.replace(hour=00, minute=00, second=00) + \
        datetime.timedelta(days=1)
    yield todate, end_date

def split_date(start_date, end_date, div):
    delta = date_delta(start_date, end_date, div)
    print(delta)
    return date_span(start_date, end_date, delta)
