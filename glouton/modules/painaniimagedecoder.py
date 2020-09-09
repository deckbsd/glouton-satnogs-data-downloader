from glouton.modules.telemetryModuleBase import TelemetryModuleBase
from glouton.modules.painaniDecoder import PainaniDecoder
import binascii
import os


class PainaniImageDecoder(TelemetryModuleBase):
    def __init__(self, wdir):
        TelemetryModuleBase.__init__(self, wdir)
        self.__decoder = PainaniDecoder()
        self.__frame_counter = 0

    def runAfterDownload(self, frame, full_path, telemetry):
        timestamp = telemetry['timestamp']
        self.__frame_counter += 1
        file = os.path.join(full_path, timestamp.replace(
            ':', '-') + "_" + str(self.__frame_counter) + ".frame")
        with open(file, 'wb') as f:
            f.write(binascii.unhexlify(frame))

    def runAfterDownloadCompleted(self, full_path):
        self.__decoder.DecodeImages(full_path, "*.frame")
