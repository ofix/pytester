'''
@author: code lighter 
@date: 2017/9/27
@desc: Reporter is a class that support export error data to
       a file. The supported file formats are JSON|HTML|Excel
@data: required input error data
@path: required save file path
'''

from selenium import *
class Reporter:
    # @data 数据
    # @path 路径
    def __init__(self,data,path):
        self.__data = data
        self.__path = path
    def toJson(self):
        return self.__data
    def toHtml(self):
        return self.__data
    def toExcel(self):
        return self.__data
    def screenShot(self):
        pass

