class EpsObj:
    def __init__(self, file):
        self._file = file
        self.name = file.stem
        print(self.name)

