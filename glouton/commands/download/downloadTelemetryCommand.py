from glouton.infrastructure.satnogDbClient import SatnogDbClient
from glouton.commands.download.downloadCommand import DownloadCommand
from glouton.commands.module.telemetryModuleCommandParams import TelemetryModuleCommandParams
from glouton.commands.module.telemetryModuleCommand import TelemetryModuleCommand
import os

class DownloadTelemetryCommand(DownloadCommand):
    def __init__(self, params, telemetry, modules_commands):
        DownloadCommand.__init__(self, params, modules_commands)
        self.telemetry = telemetry
        self.client = SatnogDbClient()

    def download(self):
        raise NotImplementedError()

    def runModulesAfterDownload(self, frame):
        if self.modules is not None:
            for module in self.modules:
                cmd_parameters = TelemetryModuleCommandParams(
                    frame, self.full_path, self.telemetry, module
                )
                moduleCommand = TelemetryModuleCommand(cmd_parameters)
                self.modules_commands.put(moduleCommand)
