from queue import Queue
from threading import Thread
from commands.download.downloadCommandParams import DownloadCommandParams
from commands.download.waterfallDownloadCommand import WaterfallDownloadCommand
from workers.downloadWorker import DownloadWorker
from workers.moduleWorker import ModuleWorker
from domain.interfaces.downloadable import Downloadable
from shared import threadHelper
from threading import Event

class WaterfallRepo(Downloadable):
    def __init__(self, working_dir, modules):
        self.__working_dir = working_dir
        self.__waterfall_commands = Queue()
        self.__waterfall_modules_commands = Queue()
        self.__modules = modules
        self.__download_status = Event()

    def register_command(self, observation, start_date, end_date):
        cmd_parameters = DownloadCommandParams(
            self.__working_dir, self.__create_dir_name('waterfall', start_date, end_date), self.__modules)
        waterfallDownloadCommand = WaterfallDownloadCommand(
            cmd_parameters, observation, self.__waterfall_modules_commands)
        self.__waterfall_commands.put(waterfallDownloadCommand)

    def create_worker(self):
        threads = []
        downloadWorker = DownloadWorker(self.__waterfall_commands, self.__download_status)
        threads.append(threadHelper.create_thread(downloadWorker.execute))
        if self.__modules is not None:
            moduleWorker = ModuleWorker(self.__waterfall_modules_commands, self.__download_status)
            threads.append(threadHelper.create_thread(moduleWorker.execute))

        return threads

    def __create_dir_name(self, target, start_date, end_date):
        return target + '__' + start_date.strftime('%m-%d-%YT%H-%M-%S') + '__' + end_date.strftime('%m-%d-%YT%H-%M-%S')
