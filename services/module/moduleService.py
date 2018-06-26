import importlib

class ModuleService:
    def __init__(self, cmd):
        self.__cmd = cmd

    def loadDemoddataModules(self):
        return self.__loadModule(self.__cmd.demoddata_modules)

    def loadPayloadModules(self):
        return self.__loadModule(self.__cmd.payload_modules)

    def loadWaterfallModules(self):
        return self.__loadModule(self.__cmd.waterfall_modules)

    def __loadModule(self, modules):
        if modules is None:
            print('No module list found')
            return None
        
        loaded_modules = []
        for name in modules:
            loaded_module = importlib.import_module('modules.' + name.lower())
            module = getattr(loaded_module, name)
            loaded_modules.append(module())
            print('module : ' + name + ' loaded')
        return loaded_modules