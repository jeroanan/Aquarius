class config(object):
    
    def __init__(self):
        self.__webServerAddress = ""
        self.__webServerPort = ""
        
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