
from glouton.modules.telemetryModuleBase import TelemetryModuleBase
import json

class Polaris(TelemetryModuleBase):
    def __init__(self, wdir):
        TelemetryModuleBase.__init__(self, wdir)
        self.count = 0

    def runAfterDownload(self, frame, full_path, telemetry):
        timestamp = telemetry['timestamp']
        if not frame:
            print('no frame for ' + timestamp)
        
        json_file = full_path + '/' + timestamp.replace(':', '-') + '.json'
        telemetry_obj = {
            "timestamp": timestamp,
            "frame": frame
        }
        json_telemetry = json.dumps(telemetry_obj)
        with open(json_file, 'a') as f:
            f.write(json_telemetry)

        self.count += 1
        print('Timestamp ' + timestamp + ' Frame ' +  frame + ' count ' + str(self.count))