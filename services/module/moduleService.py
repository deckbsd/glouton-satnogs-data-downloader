import importlib
from shared.logger import logger
from shared import config

class ModuleService:
    def __init__(self, cmd):
        self.__cmd = cmd
        self.__config = config.read()

    def loadDemoddataModules(self):
        logger.Info('Demoddata module(s) loading :')
        self.__cmd.demoddata_modules = self.__getModulesFromConfig(self.__cmd.demoddata_modules, 'DEMODDATA')
        self.__cmd.demoddata_modules = self.__getModulesFromConfig(self.__cmd.demoddata_modules, 'FORALL')
        
        return self.__loadModule(self.__cmd.demoddata_modules)

    def loadPayloadModules(self):
        logger.Info('Payload module(s) loading :')
        self.__cmd.payload_modules = self.__getModulesFromConfig(self.__cmd.payload_modules, 'PAYLOAD')
        self.__cmd.payload_modules = self.__getModulesFromConfig(self.__cmd.payload_modules, 'FORALL')

        return self.__loadModule(self.__cmd.payload_modules)

    def loadWaterfallModules(self):
        logger.Info('Waterfall module(s) loading :')
        self.__cmd.waterfall_modules = self.__getModulesFromConfig(self.__cmd.waterfall_modules, 'WATERFALL')
        self.__cmd.waterfall_modules = self.__getModulesFromConfig(self.__cmd.waterfall_modules, 'FORALL')

        return self.__loadModule(self.__cmd.waterfall_modules)

    def __loadModule(self, modules):
        if modules is None:
            logger.Info('No module list found')
            return None
        
        loaded_modules = []
        for name in modules:
            loaded_module = importlib.import_module('modules.' + name.lower())
            module = getattr(loaded_module, name)
            loaded_modules.append(module(self.__cmd.working_dir))
            logger.Info('module : ' + name + ' loaded')
        return loaded_modules

    def __getModulesFromConfig(self, modules, config_array_name):
        modules_from_config = self.__config['MODULES'][config_array_name]
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