
from glouton.modules.moduleBase import ModuleBase

class TestModule(ModuleBase):

    def runAfterDownload(self, file_name, full_path, observation):
        print('executed after ' +  file_name)