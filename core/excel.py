import xlrd
class Excel:
    def __init__(self,filePath):
        self._filePath = filePath
        self._error = []
    def write(self,header,data):
        self._header = header
        self._data = data
    def read(self):
        pass
    def open(self):
        try:
            data = xlrd.open_workbook(self._filePath)
            return data
        except Exception as e:
            self._data.push(e)

