class DownloadWorker:
    def __init__(self, queue):
        self._commands = queue

    def execute(self):
        while self._commands.empty() == False:
            command = self._commands.get()
            command.download()
            self._commands.task_done()