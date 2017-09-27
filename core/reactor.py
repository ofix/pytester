from multiprocessing import Queue
from core.page import Page
class Reactor:
    def __init__(self,context):
        self.__mode = 'single'
        self.__page = ''
        self.__context = context
        self.__queue = Queue(500)
    def setRunMode(self,mode):
        allow_mode = ['single','batch']
        if not mode in allow_mode:
            raise Exception('unsupported reactor run mode.')
        self.__mode = mode
    def getRunMode(self):
        return self.__mode
    def run(self):
        if isinstance(self.__page,Page):
            self.__page.execute()
    def push(self,page):
        if not isinstance(page,Page):
            raise Exception('parameter is not a Page object.')
        self.__queue.put(Page)
    def shutdown(self):
        if(self.__mode == 'single'):
            if(isinstance(self.__page,Page)):
                self.__page.shutdown()
        else:
            while(self.__queue.qsize()):
                page = self.__queue.get()
                page.shutdown()