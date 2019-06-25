from glouton.modules.moduleBase import ModuleBase
from time import strftime, strptime
from datetime import datetime

# This module writes out decoded telemetry frames in the same format
# provided by the telemetry download option on db.satnogs.org.
class CSV(ModuleBase):

    def runAfterDownload(self, file_name, full_path, observation):
        csv_file = full_path + '/' + file_name + '.csv'

        # FIXME: The date format appears to be RFC 3339; haven't found
        # a better way of parsing this than this format string, which
        # assumes that it'll end in Z.
        dobj = datetime.strptime(observation['start'], '%Y-%m-%dT%H:%M:%SZ')
        obs_time = dobj.strftime('%Y-%m-%d %H:%M:%S')

        with open(full_path + '/' + file_name, 'rb') as f:
            hexdump = f.read().hex().upper()
        with open(csv_file, 'w') as f:
            f.write(obs_time + '|' + hexdump + '\n')
