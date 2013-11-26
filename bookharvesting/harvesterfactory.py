from bookharvesting.filesystemharvester import filesystemharvester
from bookharvesting.hardcodedharvester import hardcodedharvester

class harvesterfactory(object):
    
    def __init__(self, app):
        self.__app = app
    
    def GetHarvester(self, harvesterType):
        if harvesterType=="filesystem":
            return filesystemharvester(self.__app)
        return hardcodedharvester(self.__app)
    
    
