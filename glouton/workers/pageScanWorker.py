from glouton.shared.logger import logger


class PageScanWorker:
    def __init__(self, client, cmd, repos, path, url_params, job_number):
        self.PATH = path
        self.__client = client
        self.__cmd = cmd
        self.__repos = repos
        self.__job_number = str(job_number)
        self.__url_params = url_params

    def scan(self):
        params = self.__url_params
        page = 1
        job_string = 'job ' + self.__job_number
        while True:
            r = self.__client.get_from_base(
                self.PATH, params)
            if r.status_code != 200:
                break

            logger.Info(job_string +
                        ' scanning page...' + params['page'])
            self.__read_page(r.json(), self.__cmd.start_date,
                             self.__cmd.end_date)
            page += 1
            params['page'] = str(page)

        logger.Info(job_string + ' terminated')

    def __read_page(self, elements, start_date, end_date):
        for element in elements:
            for repo in self.__repos:
                repo.register_command(
                    element, start_date, end_date)

