from queue import Queue
from glouton.workers.pageScanWorker import PageScanWorker
from glouton.infrastructure.satnogDbClient import SatnogDbClient
from glouton.shared import threadHelper
from glouton.shared.logger import logger
from threading import Event


class TelemetryRepo:
    def __init__(self, cmd, repos):
        self.TELEMETRY_URL = 'telemetry/'
        self.__repos = repos
        self.__cmd = cmd
        self.__threads = []

    def extract(self):
        client = SatnogDbClient()
        threads = []
        page_counter = 0
        end_signal = Event()
        while True:
            for p in range(1, 5):
                page = page_counter + p
                url_params = self.__url_param_builder(
                    self.__cmd.start_date, self.__cmd.end_date, page)
                pageScanner = PageScanWorker(
                    client, self.__cmd, self.__repos, self.TELEMETRY_URL, url_params, p, end_signal)
                t = threadHelper.create_thread(pageScanner.scan)
                threads.append(t)

            threadHelper.wait(threads)
            if end_signal.isSet():
                break

            page_counter += 4
        print('\ndownloading started (Ctrl + C to stop)...\t~(  ^o^)~')
        self.__register_end_command()
        self.__create_workers_and_wait()

    def __register_end_command(self):
        for repo in self.__repos:
            repo.register_end_command(
                self.__cmd.start_date, self.__cmd.end_date)

    def __create_workers_and_wait(self):
        for repo in self.__repos:
            self.__threads.extend(repo.create_worker())
        threadHelper.wait(self.__threads)

    def __url_param_builder(self, start_date, end_date, page):
        return {'satellite': self.__cmd.norad_id,
                'start': start_date.isoformat(),
                'end': end_date.isoformat(),
                'observer': self.__cmd.observer,
                'transmitter': self.__cmd.transmitter,
                'app_source': self.__cmd.app_source,
                'page': str(page),
                'format': 'json'}
