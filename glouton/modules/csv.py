from glouton.modules.moduleBase import ModuleBase
from time import strftime, strptime
from datetime import datetime

# This module writes out decoded telemetry frames in the same format
# provided by the telemetry download option on db.satnogs.org.
class CSV(ModuleBase):

    def runAfterDownload(self, file_name, full_path, observation):
        csv_file = full_path + '/' + file_name + '.csv'

        # extract timestamp from binary frame file name
        # the filename consists of three parts:
        # data_843421_2019-07-20T13-21-51
        # 1. prefix "data"
        # 2. observation id
        # 3. timestamp of the recorded frame in UTC
        # after the split the array index [2] contains the timestamp
        dobj = datetime.strptime(file_name.split('_')[2], '%Y-%m-%dT%H-%M-%S')
        obs_time = dobj.strftime('%Y-%m-%d %H:%M:%S')

        with open(full_path + '/' + file_name, 'rb') as f:
            hexdump = f.read().hex().upper()
        with open(csv_file, 'w') as f:
            f.write(obs_time + '|' + hexdump + '\n')
