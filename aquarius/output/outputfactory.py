from aquarius.output.console.console import console
from aquarius.output.dummy.dummy import dummy
from aquarius.output.web.web import web


class outputfactory(object):
    
    def __init__(self, app, config):
        self.__app = app
        self.__config = config
        
    def GetOutput(self, outputtype):
        if outputtype == "web":
            return web(self.__app, self.__config)
        elif outputtype == "dummy":
            return dummy()
        else:
            return console(self.__app, self.__config)
