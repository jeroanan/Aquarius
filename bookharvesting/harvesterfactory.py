from bookharvesting.filesystemharvester import filesystemharvester
from bookharvesting.hardcodedharvester import hardcodedharvester

class harvesterfactory(object):
    
    def __init__(self, app, config):
        self.__app = app
        self.__config = config
        
    def GetHarvester(self, harvesterType):
        if harvesterType=="filesystem":
            return filesystemharvester(self.__app)
        return hardcodedharvester(self.__app, self.__config)
    
    
