from output.console.console import console
from output.web.web import web

class outputfactory(object):
    
    def __init__(self, app):
        self.__app = app
        
    def GetOutput(self, outputtype):
        if outputtype == "web":
            return web(self.__app)        
        return console(self.__app)
