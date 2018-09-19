import pickle

class SessionService:
    def __init__(self):
        self.SESSION_FILENAME = ".session"

    def save_program_parameters(self, cmd):
        with open(self.SESSION_FILENAME, 'wb') as f:
            pickle.dump(cmd, f, pickle.DEFAULT_PROTOCOL)

    def load_last_program_parameters(self):
        with open(self.SESSION_FILENAME, "rb") as f:
            return pickle.load(f)
