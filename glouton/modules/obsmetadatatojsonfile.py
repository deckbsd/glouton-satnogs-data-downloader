import json

from glouton.modules.observationModuleBase import ObservationModuleBase


class ObsMetadataToJsonFile(ObservationModuleBase):

    def runAfterDownload(self, file_name, full_path, observation):
        json_file = full_path + '/' + file_name + '.json'
        with open(json_file, 'w') as f:
            f.write(json.dumps(observation, indent=4))
