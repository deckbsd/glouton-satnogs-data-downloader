from glouton.commands.module.moduleCommandParams import ModuleCommandParams

class TelemetryModuleCommandParams(ModuleCommandParams):
    def __init__(self, file_name=None, full_path=None, telemetry=None, module=None):
        ModuleCommandParams.__init__(self, file_name, full_path, module)
        self.telemetry = telemetry
