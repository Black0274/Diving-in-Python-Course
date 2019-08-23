import tempfile


class FileReader:

    def __init__(self, epath):
        self.path = epath

    def read(self):
        try:
            with open(self.path, 'r') as f:
                return f.read()
        except IOError:
            return ""
