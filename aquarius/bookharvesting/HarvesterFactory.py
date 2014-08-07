from aquarius.bookharvesting.FileSystemHarvester import FileSystemHarvester


class HarvesterFactory(object):

    def __init__(self, app, config):
        self.__app = app
        self.__config = config

    def get_harvester(self):
        return FileSystemHarvester(self.__app, self.__config)
