from glouton.commands.module.moduleCommandParams import ModuleCommandParams


class ObservationModuleCommandParams(ModuleCommandParams):
    def __init__(self, file_name=None, full_path=None, observation=None, module=None):
        ModuleCommandParams.__init__(self, file_name, full_path, module)
        self.observation = observation
