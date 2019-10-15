from queue import Queue
from threading import Thread
from glouton.commands.download.downloadCommandParams import DownloadCommandParams
from glouton.commands.download.frameDownloadCommand import FrameDownloadCommand
from glouton.workers.downloadWorker import DownloadWorker
from glouton.workers.moduleWorker import ModuleWorker
from glouton.domain.interfaces.downloadable import Downloadable
from glouton.shared import threadHelper
from threading import Event


class FrameRepo(Downloadable):
    def __init__(self, working_dir, modules):
        self.__working_dir = working_dir
        self.__frame_commands = Queue()
        self.__frame_modules_commands = Queue()
        self.__modules = modules
        self.__download_status = Event()

    def register_command(self, telemetry, start_date, end_date):
        cmd_parameters = DownloadCommandParams(
            self.__working_dir, self.__create_dir_name('frames', start_date, end_date), self.__modules)
        waterfallDownloadCommand = FrameDownloadCommand(
            cmd_parameters, telemetry, self.__frame_modules_commands)
        self.__frame_commands.put(waterfallDownloadCommand)

    def create_worker(self):
        threads = []
        downloadWorker = DownloadWorker(
            self.__frame_commands, self.__download_status)
        threads.append(threadHelper.create_thread(downloadWorker.execute))
        if self.__modules is not None:
            moduleWorker = ModuleWorker(
                self.__frame_modules_commands, self.__download_status)
            threads.append(threadHelper.create_thread(moduleWorker.execute))

        return threads

    def __create_dir_name(self, target, start_date, end_date):
        return target + '__' + start_date.strftime('%m-%d-%YT%H-%M-%S') + '__' + end_date.strftime('%m-%d-%YT%H-%M-%S')
