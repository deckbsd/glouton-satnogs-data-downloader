from shared.logger import logger

class DownloadWorker:
    def __init__(self, queue):
        self._commands = queue

    def execute(self):
        try:
            while self._commands.empty() == False:
                command = self._commands.get()
                command.download()
                self._commands.task_done()
        except Exception as ex:
            logger.Error(ex)