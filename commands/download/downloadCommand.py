from infrastructure.satnogClient import SatnogClient
from commands.module.moduleCommandParams import ModuleCommandParams
from commands.module.moduleCommand import ModuleCommand
import os

class DownloadCommand:
    def __init__(self, params, observation, modules_commands):
        self.observation = observation
        self.client = SatnogClient()
        self.full_path = os.path.join(params.working_dir, params.sub_folder)
        self.modules = params.modules
        self.modules_commands = modules_commands

    def download(self):
        raise NotImplementedError()

    def runModulesAfterDownload(self, file_name):
        if self.modules is not None:
            for module in self.modules:
                cmd_parameters = ModuleCommandParams(
                    file_name, self.full_path, self.observation, module
                )
                moduleCommand = ModuleCommand(cmd_parameters)
                self.modules_commands.put(moduleCommand)