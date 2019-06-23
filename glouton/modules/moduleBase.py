from glouton.infrastructure.satnogClient import SatnogClient
import os

class ModuleBase:
    def __init__(self, working_dir):
        self.working_dir = working_dir

    def runAfterDownload(self, file_name, full_path, observation):
        raise NotImplementedError()
