from output.console.console import console
from output.web.web import web

class outputfactory(object):
    
    def __init__(self, app, config):
        self.__app = app
        self.__config = config
        
    def GetOutput(self, outputtype):
        if outputtype == "web":
            return web(self.__app, self.__config)        
        return console(self.__app, self.__config)
