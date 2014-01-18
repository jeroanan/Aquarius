class Config(object):
    
    def __init__(self):
        self.__sqlLiteDatabasePath = "./aquarius.db"
        self.__webServerAddress = ""
        self.__webServerPort = 9090
        self.__harvestPaths = []
        
    @property
    def harvest_paths(self):
        return self.__harvestPaths
    
    @harvest_paths.setter
    def harvest_paths(self, value):
        self.__harvestPaths = value
    
    @property
    def sqllite_database_path(self):
        return self.__sqlLiteDatabasePath
    
    @sqllite_database_path.setter
    def sqllite_database_path(self, value):
        self.__sqlLiteDatabasePath = value
        
    @property
    def web_server_address(self):
        return self.__webServerAddress
    
    @web_server_address.setter
    def web_server_address(self, value):
        self.__webServerAddress = value
        
    @property
    def web_server_port(self):
        return self.__webServerPort
    
    @web_server_port.setter
    def web_server_port(self, value):
        self.__webServerPort = value
