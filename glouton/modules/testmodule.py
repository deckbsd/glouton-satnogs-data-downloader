
from glouton.modules.observationModuleBase import ObservationModuleBase

class TestModule(ObservationModuleBase):

    def runAfterDownload(self, file_name, full_path, observation):
        print("executed after " +  file_name)

    def runAfterDownloadCompleted(self, full_path):
        print("executed after the download finished")