from queue import Queue
from threading import Thread
from glouton.commands.download.downloadCommandParams import DownloadCommandParams
from glouton.commands.download.demoddataDownloadCommand import DemoddataDownloadCommand
from glouton.commands.module.endModuleCommand import EndModuleCommand
from glouton.commands.module.endModuleCommandParams import EndModuleCommandParams
from glouton.workers.downloadWorker import DownloadWorker
from glouton.workers.moduleWorker import ModuleWorker
from glouton.workers.endModuleWorker import EndModuleWorker
from glouton.domain.interfaces.downloadable import Downloadable
from glouton.shared import threadHelper
from threading import Event
import os


class DemoddataRepo(Downloadable):
    def __init__(self, working_dir, modules, end_modules):
        self.__working_dir = working_dir
        self.__demoddata_commands = Queue()
        self.__demoddata_modules_commands = Queue()
        self.__demoddata_end_modules_commands = Queue()
        self.__modules = modules
        self.__end_modules = end_modules
        self.__download_status = Event()
        self.__is_download_finished = Event()

    def register_download_command(self, observation, start_date, end_date):
        cmd_parameters = DownloadCommandParams(
            self.__working_dir, self.__create_dir_name('demoddata', start_date, end_date), self.__modules)
        demoddata_download_command = DemoddataDownloadCommand(
            cmd_parameters, observation, self.__demoddata_modules_commands)
        self.__demoddata_commands.put(demoddata_download_command)

    def register_end_command(self, start_date, end_date):
        if self.__end_modules is not None:
            dir_name = self.__create_dir_name(
                'demoddata', start_date, end_date)
            module_parameters = EndModuleCommandParams(full_path=os.path.join(
                self.__working_dir, dir_name), modules=self.__end_modules)
            demoddata_end_module_command = EndModuleCommand(
                module_parameters)
            self.__demoddata_end_modules_commands.put(
                demoddata_end_module_command)

    def create_worker(self):
        threads = []
        downloadWorker = DownloadWorker(
            self.__demoddata_commands, self.__download_status, self.__is_download_finished if self.__modules is None else None)
        threads.append(threadHelper.create_thread(downloadWorker.execute))
        if self.__modules is not None:
            moduleWorker = ModuleWorker(
                self.__demoddata_modules_commands, self.__download_status, self.__is_download_finished)
            threads.append(threadHelper.create_thread(moduleWorker.execute))

        if self.__end_modules is not None:
            endWorker = EndModuleWorker(
                self.__demoddata_end_modules_commands, self.__is_download_finished)
            threads.append(threadHelper.create_thread(endWorker.execute()))

        return threads

    def __create_dir_name(self, target, start_date, end_date):
        return target + '__' + start_date.strftime('%m-%d-%YT%H-%M-%S') + '__' + end_date.strftime('%m-%d-%YT%H-%M-%S')
