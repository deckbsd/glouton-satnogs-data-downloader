from queue import Queue
from glouton.shared import dateHelper
from glouton.workers.pageScanWorker import PageScanWorker
from glouton.infrastructure.satnogDbClient import SatnogDbClient
from glouton.shared import threadHelper
from glouton.shared.logger import logger


class TelemetryRepo:
    def __init__(self, cmd, repos):
        self.TELEMETRY_URL = 'telemetry/'
        self.__repos = repos
        self.__cmd = cmd
        self.__threads = []

    def extract(self):
        client = SatnogDbClient()
        diff_days = dateHelper.diff_days(
            self.__cmd.start_date, self.__cmd.end_date)
        if diff_days < 8:
            # no thread needed
            url_params = self.__url_param_builder(
                self.__cmd.start_date, self.__cmd.end_date)
            pageScanner = PageScanWorker(
                client, self.__cmd, self.__repos, self.TELEMETRY_URL, url_params, 1)
            pageScanner.scan()
        else:
            threads = []
            job = 1
            for from_datetime, to_datetime in dateHelper.split_date(self.__cmd.start_date, self.__cmd.end_date, 4):
                print(str(from_datetime) + " " + str(to_datetime))
                url_params = self.__url_param_builder(
                    from_datetime, to_datetime)
                pageScanner = PageScanWorker(
                    client, self.__cmd, self.__repos, self.TELEMETRY_URL, url_params, job)
                t = threadHelper.create_thread(pageScanner.scan)
                threads.append(t)
                job += 1

            threadHelper.wait(threads)
        print('\ndownloading started (Ctrl + C to stop)...\t~(  ^o^)~')
        self.__create_workers_and_wait()

    def __create_workers_and_wait(self):
        for repo in self.__repos:
            self.__threads.extend(repo.create_worker())
        threadHelper.wait(self.__threads)

    def __url_param_builder(self, start_date, end_date):
        return {'satellite': self.__cmd.norad_id,
                'start': start_date.isoformat(),
                'end': end_date.isoformat(),
                'observer': self.__cmd.observer,
                'transmitter': self.__cmd.transmitter,
                'app_source': self.__cmd.app_source,
                'page': '1',
                'format': 'json'}
