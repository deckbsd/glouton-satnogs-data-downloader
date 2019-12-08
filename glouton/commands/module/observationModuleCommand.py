from glouton.commands.module.moduleCommand import ModuleCommand


class ObservationModuleCommand(ModuleCommand):
    def __init__(self, params):
        ModuleCommand.__init__(self, params)

    def process(self):
        self.params.module.runAfterDownload(
            self.params.file_name, self.params.full_path, self.params.observation)
