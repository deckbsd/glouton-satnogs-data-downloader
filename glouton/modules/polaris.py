
from glouton.modules.telemetryModuleBase import TelemetryModuleBase
import json
import os


class Polaris(TelemetryModuleBase):
    def __init__(self, wdir):
        TelemetryModuleBase.__init__(self, wdir)
        self.count = 0

    def runAfterDownload(self, frame, full_path, telemetry):
        timestamp = telemetry['timestamp']
        if not frame:
            print('no frame for ' + timestamp)

        json_file = full_path + '/' + timestamp.replace(':', '-') + '.json'
        if os.path.exists(json_file):
            with open(json_file) as json_file_read:
                telemetry = json.load(json_file_read)
                telemetry['telemetry'].append({
                    "timestamp": timestamp,
                    "frame": frame
                })
            telemetry_obj = telemetry
        else:
            telemetry_obj = {"telemetry": [{
                "timestamp": timestamp,
                "frame": frame
            }]}

        json_telemetry = json.dumps(telemetry_obj)
        with open(json_file, 'w') as f:
            f.write(json_telemetry)

        self.count += 1
        print('Timestamp ' + timestamp + ' Frame ' +
              frame + ' count ' + str(self.count))
