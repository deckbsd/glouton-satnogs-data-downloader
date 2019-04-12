from queue import Queue
from threading import Thread
from commands.download.downloadCommandParams import DownloadCommandParams
from commands.download.demoddataDownloadCommand import DemoddataDownloadCommand
from workers.downloadWorker import DownloadWorker
from workers.moduleWorker import ModuleWorker
from domain.interfaces.downloadable import Downloadable
from shared import threadHelper
from threading import Event

class DemoddataRepo(Downloadable):
    def __init__(self, working_dir, modules):
        self.__working_dir = working_dir
        self.__demoddata_commands = Queue()
        self.__demoddate_modules_commands = Queue()
        self.__modules = modules
        self.__download_status = Event()

    def register_command(self, observation, start_date, end_date):
        cmd_parameters = DownloadCommandParams(
            self.__working_dir, self.__create_dir_name('demoddata', start_date, end_date), self.__modules)
        demoddataDownloadCommand = DemoddataDownloadCommand(
            cmd_parameters, observation, self.__demoddate_modules_commands)
        self.__demoddata_commands.put(demoddataDownloadCommand)

    def create_worker(self):
        threads = []
        downloadWorker = DownloadWorker(self.__demoddata_commands, self.__download_status)
        threads.append(threadHelper.create_thread(downloadWorker.execute))
        if self.__modules is not None:
            moduleWorker = ModuleWorker(self.__demoddate_modules_commands, self.__download_status)
            threads.append(threadHelper.create_thread(moduleWorker.execute))

        return threads 

    def __create_dir_name(self, target, start_date, end_date):
        return target + '__' + start_date.strftime('%m-%d-%YT%H-%M-%S') + '__' + end_date.strftime('%m-%d-%YT%H-%M-%S')