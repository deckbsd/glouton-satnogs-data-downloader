from glouton.shared.logger import logger


class PageScanWorker:
    def __init__(self, client, cmd, repos, path, url_params, job_number, end_signal):
        self.PATH = path
        self.__client = client
        self.__cmd = cmd
        self.__repos = repos
        self.__job_number = str(job_number)
        self.__url_params = url_params
        self.__end_signal = end_signal

    def scan(self):
        params = self.__url_params
        job_string = 'job ' + self.__job_number

        r = self.__client.get_from_base(
            self.PATH, params)
        if r.status_code != 200:
            self.__end_signal.set()
            return

        logger.Info(job_string +
                    ' scanning page...' + params['page'])
        self.__read_page(r.json(), self.__cmd.start_date,
                         self.__cmd.end_date)

        logger.Info(job_string + ' terminated')

    def __read_page(self, elements, start_date, end_date):
        for element in elements:
            for repo in self.__repos:
                repo.register_download_command(
                    element, start_date, end_date)
