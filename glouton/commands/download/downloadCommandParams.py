
class DownloadCommandParams:
    def __init__(self, working_dir=None, sub_folder=None, modules=None):
        self.working_dir = working_dir
        self.sub_folder = sub_folder
        self.modules = modules
