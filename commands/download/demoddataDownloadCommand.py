from commands.download.downloadCommand import DownloadCommand
from shared import fileHelper
from shared.logger import logger
import os
import ntpath
import requests


class DemoddataDownloadCommand(DownloadCommand):
    def __init__(self, params, observation, modules_commands):
        DownloadCommand.__init__(self, params, observation, modules_commands)
        self.__json_id = "demoddata"

    def download(self):
        demoddata = self.observation[self.__json_id]
        if not any(demoddata):
            logger.Info('no demoddata found for the observation ' + str(self.observation['id']) + ' of ' + self.observation['start'])
            return

        fileHelper.create_dir_if_not_exist(self.full_path)
        for demod in demoddata:
            file_name = ntpath.basename(demod['payload_demod'])
            full_path_file = self.full_path + os.path.sep + file_name
            if os.path.exists(full_path_file):
                logger.Warning('pass ' + file_name + '... file already exist')
                return

            r = self.client.get(demod['payload_demod'])
            if r.status_code == 200:
                logger.Info('downloading...' + file_name)
                with open(full_path_file, "wb") as file:
                    file.write(r.content)
                self.runModulesAfterDownload(file_name)