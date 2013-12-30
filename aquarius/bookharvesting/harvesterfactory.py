from aquarius.bookharvesting.filesystemharvester import filesystemharvester
from aquarius.bookharvesting.hardcodedharvester import hardcodedharvester

class harvesterfactory(object):
    
    def __init__(self, app, config):
        self.__app = app
        self.__config = config
        
    def GetHarvester(self, harvesterType):
        if harvesterType=="filesystem":
            return filesystemharvester(self.__app, self.__config)
        return hardcodedharvester(self.__app, self.__config)
    
    
