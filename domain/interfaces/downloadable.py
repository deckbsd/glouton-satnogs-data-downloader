
class Downloadable:
    def create_worker(self):
        raise NotImplementedError()

    def register_command(self):
        raise NotImplementedError()