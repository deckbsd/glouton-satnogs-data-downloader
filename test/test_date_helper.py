from datetime import datetime
from glouton.shared import dateHelper


months_equal_0 = [datetime(2019, 11, 30, 0, 0), datetime(2019, 12, 1, 23, 59, 59), datetime(2019, 12, 2, 0, 0), datetime(
    2019, 12, 3, 23, 59, 59), datetime(2019, 12, 4, 0, 0), datetime(2019, 12, 5, 23, 59, 59), datetime(2019, 12, 6, 0, 0), datetime(2019, 12, 7, 0, 0)]

months_equal_1 = [datetime(2019, 11, 1, 1, 21, 54), datetime(2019, 11, 8, 23, 59, 59), datetime(2019, 11, 9, 0, 0), datetime(
    2019, 11, 16, 23, 59, 59), datetime(2019, 11, 17, 0, 0), datetime(2019, 11, 23, 23, 59, 59), datetime(2019, 11, 24, 0, 0), datetime(2019, 12, 1, 1, 21, 54)]

months_equal_2 = [datetime(2017, 10, 19, 0, 51, 54), datetime(2017, 11, 3, 23, 59, 59), datetime(2017, 11, 4, 0, 0), datetime(
    2017, 11, 19, 23, 59, 59), datetime(2017, 11, 20, 0, 0), datetime(2017, 12, 4, 23, 59, 59), datetime(2017, 12, 5, 0, 0), datetime(2017, 12, 20, 0, 51, 54)]

months_equal_3 = [datetime(2017, 9, 19, 0, 51, 54), datetime(2017, 10, 12, 23, 59, 59), datetime(2017, 10, 13, 0, 0), datetime(
    2017, 11, 4, 23, 59, 59), datetime(2017, 11, 5, 0, 0), datetime(2017, 11, 27, 23, 59, 59), datetime(2017, 11, 28, 0, 0), datetime(2017, 12, 20, 0, 51, 54)]

months_equal_4 = [datetime(2017, 8, 19, 0, 51, 54), datetime(2017, 9, 18, 23, 59, 59), datetime(2017, 9, 19, 0, 0), datetime(
    2017, 10, 19, 23, 59, 59), datetime(2017, 10, 20, 0, 0), datetime(2017, 11, 19, 23, 59, 59), datetime(2017, 11, 20, 0, 0), datetime(2017, 12, 20, 0, 51, 54)]

months_equal_5 = [datetime(2017, 8, 19, 0, 51, 54), datetime(2017, 9, 19, 23, 59, 59), datetime(2017, 9, 20, 0, 0), datetime(
    2017, 10, 19, 23, 59, 59), datetime(2017, 10, 20, 0, 0), datetime(2017, 11, 19, 23, 59, 59), datetime(2017, 11, 20, 0, 0), datetime(2017, 12, 20, 0, 51, 54)]

months_equal_31 = [datetime(2015, 5, 1, 1, 21, 54), datetime(2015, 12, 30, 23, 59, 59), datetime(2015, 12, 31, 0, 0), datetime(
    2016, 8, 30, 23, 59, 59), datetime(2016, 8, 31, 0, 0), datetime(2017, 5, 1, 23, 59, 59), datetime(2017, 5, 2, 0, 0), datetime(2017, 12, 31, 1, 21, 54)]


def extract_dates(start_date, end_date):
    div = 4
    dates = []
    for d1, d2 in dateHelper.split_date(start_date, end_date, div):
        dates.append(d1)
        dates.append(d2)

    return dates


def test_days_diff_on_close_months():
    start_date = datetime.strptime(
        '2019-11-29T00:00:00', '%Y-%m-%dT%H:%M:%S')
    end_date = datetime.strptime(
        '2019-12-07T00:00:00', '%Y-%m-%dT%H:%M:%S')
    diff = dateHelper.diff_days(start_date, end_date)

    assert diff == 8

def test_7_days_diff():
    start_date = datetime.strptime(
        '2019-11-29T00:00:00', '%Y-%m-%dT%H:%M:%S')
    end_date = datetime.strptime(
        '2019-12-06T00:00:00', '%Y-%m-%dT%H:%M:%S')
    diff = dateHelper.diff_days(start_date, end_date)

    assert diff == 7

def test_8_days_diff():
    start_date = datetime.strptime(
        '2019-11-29T00:00:00', '%Y-%m-%dT%H:%M:%S')
    end_date = datetime.strptime(
        '2019-12-06T01:00:00', '%Y-%m-%dT%H:%M:%S')
    diff = dateHelper.diff_days(start_date, end_date)
    dates = extract_dates(start_date, end_date)
    print(dates)

    assert diff == 8

def test_days_diff_on_far_months():
    start_date = datetime.strptime(
        '2010-11-29T00:00:00', '%Y-%m-%dT%H:%M:%S')
    end_date = datetime.strptime(
        '2019-12-07T00:00:00', '%Y-%m-%dT%H:%M:%S')
    diff = dateHelper.diff_days(start_date, end_date)

    assert diff == 3295

def test_days_diff_on_same_month():
    start_date = datetime.strptime(
        '2019-12-6T00:00:00', '%Y-%m-%dT%H:%M:%S')
    end_date = datetime.strptime(
        '2019-12-07T00:00:00', '%Y-%m-%dT%H:%M:%S')
    diff = dateHelper.diff_days(start_date, end_date)

    assert diff == 1

def test_days_diff_no_days():
    start_date = datetime.strptime(
        '2019-12-07T00:00:00', '%Y-%m-%dT%H:%M:%S')
    end_date = datetime.strptime(
        '2019-12-07T00:00:00', '%Y-%m-%dT%H:%M:%S')
    diff = dateHelper.diff_days(start_date, end_date)

    assert diff == 0


def test_split_0_months_to_4_ranges():
    start_date = datetime.strptime(
        '2019-11-30T00:00:00', '%Y-%m-%dT%H:%M:%S')
    end_date = datetime.strptime(
        '2019-12-07T00:00:00', '%Y-%m-%dT%H:%M:%S')
    dates = extract_dates(start_date, end_date)

    assert dates == months_equal_0
    assert dates[0] == start_date
    assert dates[len(dates)-1] == end_date
    assert len(dates) == 8


def test_split_1_months_to_4_ranges():
    start_date = datetime.strptime(
        '2019-11-01T01:21:54', '%Y-%m-%dT%H:%M:%S')
    end_date = datetime.strptime(
        '2019-12-01T01:21:54', '%Y-%m-%dT%H:%M:%S')
    dates = extract_dates(start_date, end_date)

    assert dates == months_equal_1
    assert dates[0] == start_date
    assert dates[len(dates)-1] == end_date
    assert len(dates) == 8


def test_split_3_months_to_4_ranges():
    start_date = datetime.strptime(
        '2017-09-19T00:51:54', '%Y-%m-%dT%H:%M:%S')
    end_date = datetime.strptime(
        '2017-12-20T00:51:54', '%Y-%m-%dT%H:%M:%S')
    dates = extract_dates(start_date, end_date)

    assert dates == months_equal_3
    assert dates[0] == start_date
    assert dates[len(dates)-1] == end_date
    assert len(dates) == 8


def test_split_2_months_to_4_ranges():
    start_date = datetime.strptime(
        '2017-10-19T00:51:54', '%Y-%m-%dT%H:%M:%S')
    end_date = datetime.strptime(
        '2017-12-20T00:51:54', '%Y-%m-%dT%H:%M:%S')
    dates = extract_dates(start_date, end_date)

    assert dates == months_equal_2
    assert dates[0] == start_date
    assert dates[len(dates)-1] == end_date
    assert len(dates) == 8


def test_split_4_months_to_4_ranges():
    start_date = datetime.strptime(
        '2017-08-19T00:51:54', '%Y-%m-%dT%H:%M:%S')
    end_date = datetime.strptime(
        '2017-12-20T00:51:54', '%Y-%m-%dT%H:%M:%S')
    dates = extract_dates(start_date, end_date)

    assert dates == months_equal_4
    assert dates[0] == start_date
    assert dates[len(dates)-1] == end_date
    assert len(dates) == 8


def test_split_31_months_to_4_ranges():
    start_date = datetime.strptime(
        '2015-05-01T01:21:54', '%Y-%m-%dT%H:%M:%S')
    end_date = datetime.strptime(
        '2017-12-31T01:21:54', '%Y-%m-%dT%H:%M:%S')
    dates = extract_dates(start_date, end_date)

    assert dates == months_equal_31
    assert dates[0] == start_date
    assert dates[len(dates)-1] == end_date
    assert len(dates) == 8
