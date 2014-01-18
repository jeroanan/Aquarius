class Book(object):
    """"Holds details about an individual book in the system"""
    def __init__(self):
        """Set initial object state"""
        self.__Id = ""
        self.__author = ""
        self.__title = ""
        self.__formats = []
        self.__author_uri = ""

    @property
    def author(self):
        """Gets this book's author"""
        return self.__author

    @author.setter
    def author(self, value):
        """Sets this book's author"""
        self.__author = value

    @property
    def author_uri(self):
        """Gets a URI for this book's author"""
        return self.__author_uri

    @author_uri.setter
    def author_uri(self, value):
        """Sets a URI for this book's author"""
        self.__author_uri = value

    @property
    def title(self):
        """Gets this book's title"""
        return self.__title

    @title.setter
    def title(self, value):
        """Sets this book's title"""
        self.__title = value

    @property
    def formats(self):
        """Gets the formats stored against this book."""
        return self.__formats

    @formats.setter
    def formats(self, value):
        """Sets the formats stored against this book."""
        self.__formats = value

    @property
    def id(self):
        """Gets this book's Id"""
        return self.__Id

    @id.setter
    def id(self, value):
        """Sets this book's Id"""
        self.__Id = value

    def add_format(self, bookformat):
        """Adds a format to the book"""
        if not self.__already_have_format(bookformat):
            self.formats.append(bookformat)

    def __already_have_format(self, bookformat):
        for bf in self.formats:
            if bf == bookformat:
                return True
        return False

    def __eq__(self, other):
        """Determines whether this book is equal to another instance of book"""
        if other is None:
            return False
        return str.lower(self.author) == str.lower(other.author) \
            and str.lower(self.title) == str.lower(other.title)

    def __str__(self):
        """"Returns a string representation of this object"""
        return "%s - %s" % (self.author, self.title)
