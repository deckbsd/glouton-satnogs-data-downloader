from glouton.infrastructure.satnogNetworkClient import SatnogNetworkClient
from glouton.commands.download.downloadCommand import DownloadCommand
from glouton.commands.module.observationModuleCommandParams import ObservationModuleCommandParams
from glouton.commands.module.observationModuleCommand import ObservationModuleCommand
import os

class DownloadObservationCommand(DownloadCommand):
    def __init__(self, params, observation, modules_commands):
        DownloadCommand.__init__(self, params, modules_commands)
        self.observation = observation
        self.client = SatnogNetworkClient()

    def download(self):
        raise NotImplementedError()

    def runModulesAfterDownload(self, file_name):
        if self.modules is not None:
            for module in self.modules:
                cmd_parameters = ObservationModuleCommandParams(
                    file_name, self.full_path, self.observation, module
                )
                moduleCommand = ObservationModuleCommand(cmd_parameters)
                self.modules_commands.put(moduleCommand)
