class booktype(object):
    """Holds details on a type of book"""
    __format = ""
    __mimetype = ""
    
    @property
    def Format(self):
        """Gets the format code of this book type"""
        return self.__format
    
    @Format.setter
    def Format(self, value):
        """Sets the format of this book type"""
        self.__format = value
        
    @property
    def MimeType(self):
        """Gets the mime type associated with this book type"""
        return self.__mimetype
    
    @MimeType.setter
    def MimeType(self, value):
        """Sets the mime type associated with this book type"""
        self.__mimetype = value
