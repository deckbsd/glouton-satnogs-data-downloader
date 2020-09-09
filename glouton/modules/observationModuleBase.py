from glouton.modules.moduleBase import ModuleBase


class ObservationModuleBase(ModuleBase):
    def __init__(self, working_dir):
        ModuleBase.__init__(self, working_dir)

    def runAfterDownload(self, file_name, full_path, observation):
        raise NotImplementedError()

    def runAfterDownloadCompleted(self, full_path):
        raise NotImplementedError()
