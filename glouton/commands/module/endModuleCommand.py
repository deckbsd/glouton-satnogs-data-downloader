from glouton.commands.module.moduleCommand import ModuleCommand


class EndModuleCommand(ModuleCommand):
    def __init__(self, params):
        ModuleCommand.__init__(self, params)

    def process(self):
        for module in self.params.modules:
            module.runAfterDownloadCompleted(self.params.full_path)
