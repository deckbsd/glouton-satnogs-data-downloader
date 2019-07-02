import os

class ModuleCommand:
    def __init__(self, params):
        self.__params = params

    def process(self):
        self.__params.module.runAfterDownload(self.__params.file_name, self.__params.full_path, self.__params.observation)
