from services.module.moduleService import ModuleService
from repositories.demoddata.demoddataRepo import DemoddataRepo
from repositories.payload.payloadRepo import PayloadRepo
from repositories.waterfall.waterfallRepo import WaterfallRepo
from repositories.observation.observationsRepo import ObservationRepo

class ObservationsService:
    def __init__(self, cmd):
        self.__cmd = cmd
        self.__module_service = ModuleService(self.__cmd)
        repos = self.filter_repositories()
        self.__observations_repo = ObservationRepo(self.__cmd, repos)

    def filter_repositories(self):
        downloadable_data_repos = []
        all = not self.__cmd.payloads and not self.__cmd.waterfalls and not self.__cmd.demoddata
        if all or self.__cmd.payloads:
            downloadable_data_repos.append(PayloadRepo(self.__cmd.working_dir, self.__module_service.loadPayloadModules()))
        if all == True or self.__cmd.waterfalls:
            downloadable_data_repos.append(WaterfallRepo(self.__cmd.working_dir, self.__module_service.loadWaterfallModules()))
        if all == True or self.__cmd.demoddata:
            downloadable_data_repos.append(DemoddataRepo(self.__cmd.working_dir, self.__module_service.loadDemoddataModules()))
        
        return downloadable_data_repos

    def extract(self):
        self.__observations_repo.extract()
