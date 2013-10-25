class bookformat(object):
    
    __format = ""
    __location = ""
    
    @property
    def Format(self):
        return self.__format
    
    @Format.setter
    def Format(self, value):
        self.__format = value
        
    @property
    def Location(self):
        return self.__location
    
    @Location.setter
    def Location(self, value):
        self.__location = value