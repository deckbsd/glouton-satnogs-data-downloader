from infrastructure.satnogClient import SatnogClient
import os

class DownloadCommand:
    def __init__(self, params, observation):
        self.observation = observation
        self.client = SatnogClient()
        self.full_path = os.path.join(params.working_dir, params.sub_folder)
        self.modules = params.modules

    def download(self):
        raise NotImplementedError()

    def runModulesAfterDownload(self, file_name):
        if self.modules is not None:
            for module in self.modules:
                module.runAfterDownload(file_name, self.full_path, self.observation)