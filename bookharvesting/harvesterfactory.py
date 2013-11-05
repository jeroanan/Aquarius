from bookharvesting.hardcodedharvester import hardcodedharvester

class harvesterfactory(object):
    
    def __init__(self, app):
        self.__app = app
    
    def GetHarvester(self):
        return hardcodedharvester(self.__app)
    
    
