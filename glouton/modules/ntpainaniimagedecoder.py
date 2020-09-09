from glouton.modules.observationModuleBase import ObservationModuleBase
from glouton.modules.painaniDecoder import PainaniDecoder


class NtPainaniImageDecoder(ObservationModuleBase):
    def __init__(self, wdir):
        ObservationModuleBase.__init__(self, wdir)
        self.decoder = PainaniDecoder()

    def runAfterDownloadCompleted(self, full_path):
        self.decoder.DecodeImages(full_path, "data_*")
