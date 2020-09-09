class ModuleWorker:
    def __init__(self, queue, download_status, is_download_finished):
        self.__commands = queue
        self.__download_status = download_status
        self.__is_download_finished = is_download_finished

    def execute(self):
        while self.__commands.empty() == False or self.__download_status.isSet():
            try:
                command = self.__commands.get(block=True, timeout=1)
                command.process()
                self.__commands.task_done()
            except:
                pass

        self.__is_download_finished.set()
