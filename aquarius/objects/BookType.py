class BookType(object):
    __format = ""
    __mimetype = ""
    
    @property
    def Format(self):
        return self.__format
    
    @Format.setter
    def Format(self, value):
        self.__format = value
        
    @property
    def MimeType(self):
        return self.__mimetype
    
    @MimeType.setter
    def MimeType(self, value):
        self.__mimetype = value
