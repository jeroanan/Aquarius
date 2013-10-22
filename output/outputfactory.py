from output.console.console import console

class outputfactory(object):
    
    def __init__(self, app):
        self.__app = app
        
    def GetOutput(self, outputtype):
        return console()
