from glouton.modules.moduleBase import ModuleBase


class TelemetryModuleBase(ModuleBase):
    def __init__(self, working_dir):
        ModuleBase.__init__(self, working_dir)

    def runAfterDownload(self, frame, full_path, telemetry):
        raise NotImplementedError()

    def runAfterDownloadCompleted(self, full_path):
        raise NotImplementedError()
