class book(object):

    def __init__(self):
        self.__Id = ""       
        self.__author = ""
        self.__title = ""
        self.__formats = []
    
    @property
    def Author(self):
        return self.__author
    
    @Author.setter
    def Author(self, value):
        self.__author = value
    
    @property
    def Title(self):
        return self.__title
    
    @Title.setter
    def Title(self, value):
        self.__title = value
        
    @property
    def Formats(self):
        return self.__formats
    
    @Formats.setter
    def Formats(self, value):
        self.__formats = value
        
    @property
    def Id(self):
        return self.__Id
    
    @Id.setter
    def Id(self, value):
        self.__Id = value