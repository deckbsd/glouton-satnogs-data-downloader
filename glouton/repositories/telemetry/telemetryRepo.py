from queue import Queue
from glouton.infrastructure.satnogDbClient import SatnogDbClient
from glouton.shared.logger import logger


class TelemetryRepo:
    def __init__(self, cmd, repos):
        self.TELEMETRY_URL = 'telemetry/'
        self.__client = SatnogDbClient()
        self.__repos = repos
        self.__cmd = cmd
        self.__threads = []

    def extract(self):
        params = self.__create_request_params()
        limit = int(self.__cmd.page_to)
        page = int(self.__cmd.page_from)
        while True:
            r = self.__client.get_from_base(
                self.TELEMETRY_URL, params)
            if r.status_code != 200:
                break

            logger.Info('scanning page...' + params['page'])
            self.__read_page(r.json(), self.__cmd.page_from, self.__cmd.page_to)
            page += 1
            if page > limit:
                break

            params['page'] = str(page)

        print('\ndownloading started (Ctrl + C to stop)...\t~(  ^o^)~')
        self.__create_workers_and_wait()

    def __create_workers_and_wait(self):
        for repo in self.__repos:
            for i in range(1, 3):
                self.__threads.extend(repo.create_worker())
        while self.__is_one_thread_alive():
            for t in self.__threads:
                # let's control to main thread every seconds (in order to be able to capture Ctrl + C if needed)
                t.join(1)

    def __is_one_thread_alive(self):
        for thread in self.__threads:
            if thread.is_alive():
                return True

        return False

    def __read_page(self, telemetries, page_from, page_to):
        for telemetry in telemetries:
            for repo in self.__repos:
                repo.register_command(
                    telemetry, page_from, page_to)

    def __create_request_params(self):
        return {'satellite': self.__cmd.norad_id,
        #'start': self.__cmd.start_date.isoformat(),
        #'end': self.__cmd.end_date.isoformat(),
        'observer': self.__cmd.observer,
        'transmitter': self.__cmd.transmitter,
        'app_source': self.__cmd.app_source,
        'page': self.__cmd.page_from,
        'format': 'json'}
