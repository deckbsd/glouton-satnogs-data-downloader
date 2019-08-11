from glouton.infrastructure.satnogNetworkClient import SatnogNetworkClient
from glouton.commands.module.moduleCommandParams import ModuleCommandParams
from glouton.commands.module.moduleCommand import ModuleCommand
import os

class DownloadCommand:
    def __init__(self, params, modules_commands):
        self.full_path = os.path.join(params.working_dir, params.sub_folder)
        self.modules = params.modules
        self.modules_commands = modules_commands

    def download(self):
        raise NotImplementedError()

    def runModulesAfterDownload(self, file_name):
        raise NotImplementedError()
