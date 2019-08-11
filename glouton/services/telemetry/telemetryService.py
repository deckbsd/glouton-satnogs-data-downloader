from glouton.services.module.moduleService import ModuleService
from glouton.repositories.frame.frameRepo import FrameRepo
from glouton.repositories.telemetry.telemetryRepo import TelemetryRepo

class TelemetryService:
    def __init__(self, cmd):
        self.__cmd = cmd
        self.__module_service = ModuleService(self.__cmd)
        repos = self.filter_repositories()
        self.__telemetry_repo = TelemetryRepo(self.__cmd, repos)

    def filter_repositories(self):
        downloadable_data_repos = []
        downloadable_data_repos.append(FrameRepo(self.__cmd.working_dir, self.__module_service.loadFrameModules()))
        
        return downloadable_data_repos

    def extract(self):
        self.__telemetry_repo.extract()