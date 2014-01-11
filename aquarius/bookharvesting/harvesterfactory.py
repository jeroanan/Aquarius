from aquarius.bookharvesting.filesystemharvester import filesystemharvester
from aquarius.bookharvesting.hardcodedharvester import hardcodedharvester


class harvesterfactory(object):
    """Takes a string and instantiates the correct harvester object
    based on it"""
    def __init__(self, app, config):
        """Set initial object state"""
        self.__app = app
        self.__config = config

    def GetHarvester(self, harvester_type):
        """Get the correct harvester object according to harvestertype"""
        if harvester_type == "filesystem":
            return filesystemharvester(self.__app, self.__config)
        return hardcodedharvester(self.__app, self.__config)
