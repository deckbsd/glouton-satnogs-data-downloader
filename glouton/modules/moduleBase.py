import os

class ModuleBase:
    def __init__(self, working_dir):
        self.working_dir = working_dir

    def runAfterDownload(self, file_name, full_path, observation):
        raise NotImplementedError()

    def runAfterDownloadCompleted(self, full_path):
        raise NotImplementedError()