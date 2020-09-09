from queue import Queue
from glouton.shared.logger import logger
from glouton.shared import dateHelper
from glouton.workers.pageScanWorker import PageScanWorker
from glouton.shared import threadHelper
from glouton.infrastructure.satnogNetworkClient import SatnogNetworkClient


class ObservationRepo:
    def __init__(self, cmd, repos):
        self.OBSERVATION_URL = 'observations/'
        self.__repos = repos
        self.__cmd = cmd
        self.__threads = []

    def extract(self):
        client = SatnogNetworkClient()
        diff_days = dateHelper.diff_days(
            self.__cmd.start_date, self.__cmd.end_date)
        if diff_days < 8:
            # no thread needed
            url_params = self.__url_param_builder(
                self.__cmd.start_date, self.__cmd.end_date)
            pageScanner = PageScanWorker(
                client, self.__cmd, self.__repos, self.OBSERVATION_URL, url_params, 1)
            pageScanner.scan()
        else:
            threads = []
            job = 1
            for from_datetime, to_datetime in dateHelper.split_date(self.__cmd.start_date, self.__cmd.end_date, 4):
                print(str(from_datetime) + " " + str(to_datetime))
                url_params = self.__url_param_builder(
                    from_datetime, to_datetime)
                pageScanner = PageScanWorker(
                    client, self.__cmd, self.__repos, self.OBSERVATION_URL, url_params, job)
                t = threadHelper.create_thread(pageScanner.scan)
                threads.append(t)
                job += 1

            threadHelper.wait(threads)
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

    def __url_param_builder(self, start_date, end_date):
        return {'satellite__norad_cat_id': self.__cmd.norad_id,
                'ground_station': self.__cmd.ground_station_id,
                'start': start_date.isoformat(),
                'end': end_date.isoformat(),
                'vetted_status': self.__cmd.observation_status,
                'vetted_user': self.__cmd.user,
                'transmitter_uuid': self.__cmd.transmitter_uuid,
                'transmitter_mode': self.__cmd.transmitter_mode,
                'transmitter_type': self.__cmd.transmitter_type,
                'page': '1',
                'format': 'json'}
