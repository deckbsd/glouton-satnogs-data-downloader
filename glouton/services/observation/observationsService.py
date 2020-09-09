from glouton.services.module.moduleService import ModuleService
from glouton.repositories.demoddata.demoddataRepo import DemoddataRepo
from glouton.repositories.archive.archiveRepo import ArchiveRepo
from glouton.repositories.waterfall.waterfallRepo import WaterfallRepo
from glouton.repositories.observation.observationsRepo import ObservationRepo


class ObservationsService:
    def __init__(self, cmd):
        self.__cmd = cmd
        self.__module_service = ModuleService(self.__cmd.working_dir)
        repos = self.filter_repositories()
        self.__observations_repo = ObservationRepo(self.__cmd, repos)

    def filter_repositories(self):
        downloadable_data_repos = []
        all = not self.__cmd.archives and not self.__cmd.waterfalls and not self.__cmd.demoddata
        if all or self.__cmd.archives:
            downloadable_data_repos.append(ArchiveRepo(
                self.__cmd.working_dir, self.__module_service.loadArchiveModules(self.__cmd.archive_modules, 'FOR_EACH'), self.__module_service.loadArchiveModules(self.__cmd.archive_end_modules, 'END')))
        if all == True or self.__cmd.waterfalls:
            downloadable_data_repos.append(WaterfallRepo(
                self.__cmd.working_dir, self.__module_service.loadWaterfallModules(self.__cmd.waterfall_modules, 'FOR_EACH'), self.__module_service.loadWaterfallModules(self.__cmd.waterfall_end_modules, 'END')))
        if all == True or self.__cmd.demoddata:
            downloadable_data_repos.append(DemoddataRepo(
                self.__cmd.working_dir, self.__module_service.loadDemoddataModules(self.__cmd.demoddata_modules, 'FOR_EACH'), self.__module_service.loadDemoddataModules(self.__cmd.demoddata_end_modules, 'END')))

        return downloadable_data_repos

    def extract(self):
        self.__observations_repo.extract()
