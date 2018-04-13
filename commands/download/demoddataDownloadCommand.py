from commands.download.downloadCommand import DownloadCommand
from shared import fileHelper
import os
import ntpath
import requests


class DemoddataDownloadCommand(DownloadCommand):
    def __init__(self, params, observation):
        DownloadCommand.__init__(self, params, observation)
        self.__json_id = "demoddata"

    def download(self):
        demoddata = self.observation[self.__json_id]
        if not any(demoddata):
            print('no demoddata found for the observation ' + str(self.observation['id']) + ' of ' + self.observation['start'])
            return

        fileHelper.create_dir_if_not_exist(self.full_path)
        for demod in demoddata:
            r = self.client.get(demod['payload_demod'])
            if r.status_code == 200:
                file_name = ntpath.basename(demod['payload_demod'])
                print('downloading...' + file_name)
                with open(self.full_path + os.path.sep + file_name, "wb") as file:
                    file.write(r.content)