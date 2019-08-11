class ModuleCommand:
    def __init__(self, params):
        self.params = params

    def process(self):
        raise NotImplementedError()
