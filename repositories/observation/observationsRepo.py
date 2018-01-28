from shared import config
from queue import Queue
from infrastructure.satnogClient import SatnogClient
from repositories.waterfall.waterfallRepo import WaterfallRepo
from repositories.payload.payloadRepo import PayloadRepo


class ObservationRepo:
    def __init__(self, cmd):
        self.OBSERVATION_URL = 'observations/'
        self.__config = config.read()
        self.__client = SatnogClient()
        self.__waterfal_repo = WaterfallRepo(cmd.working_dir)
        self.__payload_repo = PayloadRepo(cmd.working_dir)
        self.__cmd = cmd

    def extract(self):
        params = self.__create_request_params()
        page = 1
        while True:
            r = self.__client.get_from_base(
                self.OBSERVATION_URL, params)
            if r.status_code != 200:
                break

            self.__read_page(r.json(), self.__cmd.start_date, self.__cmd.end_date)
            page += 1
            params['page'] = str(page)

        print('\ndownloading started (Ctrl + F5 to stop)...\t~(  ^o^)~')
        self.__create_workers_and_wait()

    def __create_workers_and_wait(self):
        threads = []
        threads.append(self.__payload_repo.create_payload_worker())
        threads.append(self.__waterfal_repo.create_waterfall_worker())
        while threads[0].is_alive() or threads[1].is_alive():
            for t in threads:
                # let's control to main thread every seconds (in order to be able to capture Ctrl + C if needed)
                t.join(1)

    def __read_page(self, observations, start_date, end_date):
        for observation in observations:
            self.__waterfal_repo.register_command(
                observation, start_date, end_date)
            self.__payload_repo.register_command(
                observation, start_date, end_date)

    def __create_request_params(self):
        return {'norad': self.__cmd.norad_id, 'start': self.__cmd.start_date.isoformat(
        ), 'end': self.__cmd.end_date.isoformat(), 'page': '1', 'format': 'json'}
