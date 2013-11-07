class config(object):
    
    def __init__(self):
        self.__webServerAddress = "192.168.2.5"
        self.__webServerPort = 9090
        self.__sqlLiteDatabasePath = "."
        
    @property
    def WebServerAddress(self):
        return self.__webServerAddress
    
    @WebServerAddress.setter
    def WebServerAddress(self, value):
        self.__webServerAddress = value
        
    @property
    def WebServerPort(self):
        return self.__webServerPort
    
    @WebServerPort.setter
    def WebServerPort(self, value):
        self.__webServerPort = value
        
    @property
    def SqlLiteDatabasePath(self):
        return self.__sqlLiteDatabasePath
    
    @SqlLiteDatabasePath.setter
    def SqlLiteDatabasePath(self, value):
        self.__sqlLiteDatabasePath = value
        