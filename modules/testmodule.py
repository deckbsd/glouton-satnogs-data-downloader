
from modules.moduleBase import ModuleBase

class TestModule(ModuleBase):

    def runAfterDownload(self, file_name, full_path):
        print('executed after ' +  file_name)