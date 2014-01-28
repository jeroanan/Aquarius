class Book(object):

    def __init__(self):
        self.__Id = ""
        self.__author = ""
        self.__title = ""
        self.__formats = []
        self.__author_uri = ""

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def author_uri(self):
        return self.__author_uri

    @author_uri.setter
    def author_uri(self, value):
        self.__author_uri = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def formats(self):
        return self.__formats

    @formats.setter
    def formats(self, value):
        self.__formats = value

    @property
    def id(self):
        return self.__Id

    @id.setter
    def id(self, value):
        self.__Id = value

    def add_format(self, bookformat):
        if not self.__already_have_format(bookformat):
            self.formats.append(bookformat)

    def __already_have_format(self, bookformat):
        for bf in self.formats:
            if bf == bookformat:
                return True
        return False

    def __eq__(self, other):
        if other is None:
            return False
        return str.lower(self.author) == str.lower(other.author) \
            and str.lower(self.title) == str.lower(other.title)

    def __str__(self):
        return "%s - %s" % (self.author, self.title)
