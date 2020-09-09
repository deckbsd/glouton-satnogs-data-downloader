import importlib
from glouton.shared.logger import logger
from glouton.shared import config


class ModuleService:
    def __init__(self, working_dir):
        self.__working_dir = working_dir
        self.__config = config.read()

    def loadDemoddataModules(self, demoddata_modules, when):
        logger.Info('(' + when + ') Demoddata module(s) loading :')
        demoddata_modules = self.__getModulesFromConfig(
            demoddata_modules, when, 'DEMODDATA')
        demoddata_modules = self.__getModulesFromConfig(
            demoddata_modules, when, 'FOR_ALL_OBSERVATION')

        return self.__loadModule(demoddata_modules)

    def loadArchiveModules(self, archive_modules, when):
        logger.Info('(' + when + ') Archive module(s) loading :')
        archive_modules = self.__getModulesFromConfig(
            archive_modules, when, 'ARCHIVE')
        archive_modules = self.__getModulesFromConfig(
            archive_modules, when, 'FOR_ALL_OBSERVATION')

        return self.__loadModule(archive_modules)

    def loadWaterfallModules(self, waterfall_modules, when):
        logger.Info('(' + when + ') Waterfall module(s) loading :')
        waterfall_modules = self.__getModulesFromConfig(
            waterfall_modules, when, 'WATERFALL')
        waterfall_modules = self.__getModulesFromConfig(
            waterfall_modules, when, 'FOR_ALL_OBSERVATION')

        return self.__loadModule(waterfall_modules)

    def loadFrameModules(self, frame_modules, when):
        logger.Info('(' + when + ') Frame module(s) loading :')
        frame_modules = self.__getModulesFromConfig(
            frame_modules, when, 'FRAME')

        return self.__loadModule(frame_modules)

    def __loadModule(self, modules):
        if modules is None:
            logger.Info('No module list found')
            return None

        loaded_modules = []
        for name in modules:
            loaded_module = importlib.import_module(
                'glouton.modules.' + name.lower())
            module = getattr(loaded_module, name)
            loaded_modules.append(module(self.__working_dir))
            logger.Info('module : ' + name + ' loaded')
        return loaded_modules

    def __getModulesFromConfig(self, modules, when, config_array_name):
        try:
            modules_from_config = self.__config['MODULES'][when][config_array_name]
        except:
            logger.Warning('config.json : modules bad format')
            modules_from_config = []

        if len(modules_from_config) == 0 and modules is None:
            return None

        if len(modules_from_config) == 0 and modules is not None:
            return modules

        if modules is None:
            modules = []

        for module in modules_from_config:
            if module in modules:
                logger.Warning('warning : ' + module + ' already referenced.')

            modules.append(module)

        return modules
