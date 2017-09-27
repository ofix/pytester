'''
Context 类
'''
from core.reactor import Reactor
class Context:
    def __init__(self):
        self.__version = '1.0.0'
        self.setEnv('local')
        self.setApp('front')
        self.__author = 'code lighter'
        self.__copy_right = 'MIT'
        self.__reactor = Reactor
    def setEnv(self,env):
        allow_env = ['local','test','dream']
        if env not in allow_env:
            raise Exception('unsupported environment in context')
        self.__env = env
    def setApp(self,app):
        allow_app = ['front','admin']
        if app not in allow_app:
            raise Exception('This app'+app+'can\'t be test')
        self.__app = app
    def version(self):
        return self.__version
    def copyright(self):
        return self.__copy_right
    def shutdown(self):
        self.__reactor.shutdown()
    def initHost(self):
        if(self.__env=='local'):
            self.host = 'http://i.ysk.dev'
        elif(self.__env=='test'):
            self.host = 'http://i.beta'


