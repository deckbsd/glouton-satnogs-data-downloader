from queue import Queue
from threading import Thread
from commands.download.downloadCommandParams import DownloadCommandParams
from commands.download.demoddataDownloadCommand import DemoddataDownloadCommand
from workers.downloadWorker import DownloadWorker
from domain.interfaces.downloadable import Downloadable

class DemoddataRepo(Downloadable):
    def __init__(self, working_dir):
        self.__working_dir = working_dir
        self.__Demoddata_commands = Queue()

    def register_command(self, observation, start_date, end_date):
        cmd_parameters = DownloadCommandParams(
            self.__working_dir, self.__create_dir_name('demoddata', start_date, end_date))
        demoddataDownloadCommand = DemoddataDownloadCommand(
            cmd_parameters, observation)
        self.__Demoddata_commands.put(demoddataDownloadCommand)

    def create_worker(self):
        return self.__create_thread(self.__Demoddata_commands)

    def __create_thread(self, queue):
        worker = DownloadWorker(queue)
        thread = Thread(target=worker.execute)
        thread.daemon = True
        thread.start()
        return thread

    def __create_dir_name(self, target, start_date, end_date):
        return target + '__' + start_date.strftime('%m-%d-%YT%H-%M-%S') + '__' + end_date.strftime('%m-%d-%YT%H-%M-%S')