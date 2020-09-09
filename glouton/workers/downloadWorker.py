from glouton.shared.logger import logger


class DownloadWorker:
    def __init__(self, queue, download_status, is_download_finished):
        self._commands = queue
        self.__download_status = download_status
        self.__is_download_finished = is_download_finished

    def execute(self):
        self.__download_status.set()
        try:
            while self._commands.empty() == False:
                command = self._commands.get()
                command.download()
                self._commands.task_done()

        except Exception as ex:
            logger.Error(ex)

        self.__download_status.clear()
        if self.__is_download_finished is not None:
            self.__is_download_finished.set()
