from glouton.commands.download.downloadCommand import DownloadCommand
from glouton.shared import fileHelper
from glouton.shared.logger import logger
import os
import ntpath
import requests


class WaterfallDownloadCommand(DownloadCommand):
    def __init__(self, params, observation, modules_commands):
        DownloadCommand.__init__(self, params, observation, modules_commands)
        self.__json_id = "waterfall"

    def download(self):
        url = self.observation[self.__json_id]
        if not url:
            logger.Info('no waterfall found for the observation ' + str(self.observation['id']) + ' of ' + self.observation['start'])
            return

        fileHelper.create_dir_if_not_exist(self.full_path)
        file_name = ntpath.basename(url)
        full_path_file = self.full_path + os.path.sep + file_name
        if os.path.exists(full_path_file):
            logger.Warning('pass ' + file_name + '... file already exist')
            return
            
        r = self.client.get(url)
        if r.status_code == 200:
            logger.Info('downloading...' + file_name)
            with open(full_path_file, "wb") as file:
                file.write(r.content)
            self.runModulesAfterDownload(file_name)
