from commands.download.downloadCommand import DownloadCommand
from shared import fileHelper
import os
import ntpath
import requests


class WaterfallDownloadCommand(DownloadCommand):
    def __init__(self, params, observation):
        DownloadCommand.__init__(self, params, observation)
        self.__json_id = "waterfall"

    def download(self):
        url = self.observation[self.__json_id]
        if not url:
            print('no waterfall found for the observation ' + str(self.observation['id']) + ' of ' + self.observation['start'])
            return

        fileHelper.create_dir_if_not_exist(self.full_path)
        r = self.client.get(url)
        if r.status_code == 200:
            file_name = ntpath.basename(url)
            print('downloading...' + file_name)
            with open(self.full_path + os.path.sep + file_name, "wb") as file:
                file.write(r.content)
