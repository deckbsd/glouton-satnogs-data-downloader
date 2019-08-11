from glouton.commands.download.downloadTelemetryCommand import DownloadTelemetryCommand
from glouton.shared import fileHelper
from glouton.shared.logger import logger
import os
import ntpath

class FrameDownloadCommand(DownloadTelemetryCommand):
    def __init__(self, params, telemetry, modules_commands):
        DownloadTelemetryCommand.__init__(self, params, telemetry, modules_commands)
        self.__json_id = "frame"

    def download(self):
        frame = self.telemetry[self.__json_id]
        if not frame:
            logger.Info('no frame found for the telemetry of ' + self.telemetry['timestamp'])
            return

        fileHelper.create_dir_if_not_exist(self.full_path)
        
        self.runModulesAfterDownload(frame)