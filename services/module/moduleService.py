import importlib
from shared.logger import logger

class ModuleService:
    def __init__(self, cmd):
        self.__cmd = cmd

    def loadDemoddataModules(self):
        logger.Info('Demoddata module(s) loading :')
        return self.__loadModule(self.__cmd.demoddata_modules)

    def loadPayloadModules(self):
        logger.Info('Payload module(s) loading :')
        return self.__loadModule(self.__cmd.payload_modules)

    def loadWaterfallModules(self):
        logger.Info('Waterfall module(s) loading :')
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