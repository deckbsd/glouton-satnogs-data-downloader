from glouton.modules.telemetryModuleBase import TelemetryModuleBase
from glouton.shared.logger import logger
import json
import os


class FlagNoImageNexusFrame(TelemetryModuleBase):
    def __init__(self, wdir):
        TelemetryModuleBase.__init__(self, wdir)
        self.types_found = []

    def runAfterDownload(self, frame, full_path, telemetry):
        timestamp = telemetry['timestamp']
        type = frame[32:34]
        if type != "C1":
            if type not in self.types_found:
                self.types_found.append(type)
            print(self.types_found)
            print("found type : " + type + " of telemetry : " + timestamp)
            file = full_path + '/' + type + "_" + timestamp.replace(':', '-') + '.frame'
            with open(file, 'w') as f:
                f.write(frame)