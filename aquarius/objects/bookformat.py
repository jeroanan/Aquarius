class bookformat(object):
    """Holds details of a particular book"""
    def __init__(self):
        """Set initial object state"""
        self.__format = ""
        self.__location = ""
    
    @property
    def Format(self):
        """Gets the format of the book"""
        return self.__format
    
    @Format.setter
    def Format(self, value):
        """Sets the format of the book"""
        self.__format = value
        
    @property
    def Location(self):
        """"Gets the location of the book"""
        return self.__location
    
    @Location.setter
    def Location(self, value):
        """"Sets the location of the book"""
        self.__location = value
        
    def __eq__(self, other):
        """Determines if this object is equal to another instance of
        BookFormat"""
        return str.lower(self.Format) == str.lower(other.Format)