from aquarius.bookharvesting.FileSystemHarvester import FileSystemHarvester
from aquarius.bookharvesting.HardcodedHarvester import HardcodedHarvester


class HarvesterFactory(object):
    """Takes a string and instantiates the correct harvester object
    based on it"""
    def __init__(self, app, config):
        """Set initial object state"""
        self.__app = app
        self.__config = config

    def get_harvester(self, harvester_type):
        """Get the correct harvester object according to harvestertype"""
        if harvester_type == "filesystem":
            return FileSystemHarvester(self.__app, self.__config)
        return HardcodedHarvester(self.__app, self.__config)
