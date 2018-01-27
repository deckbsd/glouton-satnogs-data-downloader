from infrastructure.satnogClient import SatnogClient
import os

class DownloadCommand:
    def __init__(self, params, observation):
        self.observation = observation
        self.client = SatnogClient()
        self.full_path = os.path.join(params.working_dir, params.sub_folder)

    def download(self):
        raise NotImplementedError()
