class book(object):
    """"Holds details about an individual book in the system"""
    def __init__(self):
        """Set initial object state"""
        self.__Id = ""
        self.__author = ""
        self.__title = ""
        self.__formats = []
        self.__authoruri = ""

    @property
    def Author(self):
        """Gets this book's author"""
        return self.__author

    @Author.setter
    def Author(self, value):
        """Sets this book's author"""
        self.__author = value

    @property
    def AuthorUri(self):
        """Gets a URI for this book's author"""
        return self.__authoruri

    @AuthorUri.setter
    def AuthorUri(self, value):
        """Sets a URI for this book's author"""
        self.__authoruri = value

    @property
    def Title(self):
        """Gets this book's title"""
        return self.__title

    @Title.setter
    def Title(self, value):
        """Sets this book's title"""
        self.__title = value

    @property
    def Formats(self):
        """Gets the formats stored against this book."""
        return self.__formats

    @Formats.setter
    def Formats(self, value):
        """Sets the formats stored against this book."""
        self.__formats = value

    @property
    def Id(self):
        """Gets this book's Id"""
        return self.__Id

    @Id.setter
    def Id(self, value):
        """Sets this book's Id"""
        self.__Id = value

    def AddFormat(self, bookformat):
        """Adds a format to the book"""
        if not self.__already_have_format(bookformat):
            self.Formats.append(bookformat)

    def __already_have_format(self, bookformat):
        for bf in self.Formats:
            if bf == bookformat:
                return True
        return False

    def __eq__(self, other):
        """Determines whether this book is equal to another instance of book"""
        if other is None:
            return False
        return str.lower(self.Author) == str.lower(other.Author) \
            and str.lower(self.Title) == str.lower(other.Title)

    def __str__(self):
        """"Returns a string representation of this object"""
        return "%s - %s" % (self.Author, self.Title)
