from queue import Queue
from threading import Thread
from commands.download.downloadCommandParams import DownloadCommandParams
from commands.download.payloadDownloadCommand import PayloadDownloadCommand
from workers.downloadWorker import DownloadWorker
from domain.interfaces.downloadable import Downloadable

class PayloadRepo(Downloadable):
    def __init__(self, working_dir, modules):
        self.__working_dir = working_dir
        self.__Payload_commands = Queue()
        self.__modules = modules

    def register_command(self, observation, start_date, end_date):
        cmd_parameters = DownloadCommandParams(
            self.__working_dir, self.__create_dir_name('payload', start_date, end_date), self.__modules)
        waterfallDownloadCommand = PayloadDownloadCommand(
            cmd_parameters, observation)
        self.__Payload_commands.put(waterfallDownloadCommand)

    def create_worker(self):
        return self.__create_thread(self.__Payload_commands)

    def __create_thread(self, queue):
        worker = DownloadWorker(queue)
        thread = Thread(target=worker.execute)
        thread.daemon = True
        thread.start()
        return thread

    def __create_dir_name(self, target, start_date, end_date):
        return target + '__' + start_date.strftime('%m-%d-%YT%H-%M-%S') + '__' + end_date.strftime('%m-%d-%YT%H-%M-%S')