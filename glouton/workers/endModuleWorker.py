class EndModuleWorker:
    def __init__(self, queue, download_end_status):
        self.__commands = queue
        self.__download_end_status = download_end_status

    def execute(self):
        self.__download_end_status.wait()
        while self.__commands.empty() == False:
            try:
                command = self.__commands.get()
                command.process()
                self.__commands.task_done()
            except:
                pass

        self.__download_end_status.clear()
