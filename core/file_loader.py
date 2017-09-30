class FileLoader:
    def __init__(self,filePath):
        self._filePath = filePath
        self._data = None
        oFile = open(filePath)
        try:
            self._data = oFile.read()
        finally:
            oFile.close()
    def read(self):
        return self._data
    def path(self):
        return self._filePath