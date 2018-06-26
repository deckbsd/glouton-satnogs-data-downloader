from infrastructure.satnogClient import SatnogClient
import os

class ModuleBase:
    def runAfterDownload(self, file_name, full_path):
        raise NotImplementedError()