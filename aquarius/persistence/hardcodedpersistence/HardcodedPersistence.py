from aquarius.objects.Book import Book
from aquarius.persistence.hardcodedpersistence.SetupTestBookHelper import SetupTestBookHelper
from aquarius.persistence.hardcodedpersistence.SetupTestBookTypesHelper import SetupTestBookTypesHelper


class HardcodedPersistence(object):
    """Provides a hardcoded data store. It implements the same interface as the
     other persistors but any data added to/removed from it is transient and
     forgotten between sessions, as it's all stored in memory"""

    def __init__(self, config):
        self.__books = SetupTestBookHelper().setup()
        self.book_types = SetupTestBookTypesHelper().setup()
        
    def search_books(self, search_term):
        """Searches for books in the database, returning a result set as a list
        of book objects"""
        for b in self.__books:
            if str.upper(search_term) in \
                    str.upper(b.title) and search_term != "":
                yield b

    def list_books_by_first_letter(self, first_letter):
        """Searches for books whose title begins with the given letter,
        returning a result set as a list of book objects"""
        for b in self.__books:
            if str.upper(b.title).startswith(str.upper(first_letter)):
                yield b
                
    def get_book_details(self, book_id):
        """Gets a given book by Id. Returns a book object."""
        for b in self.__books:
            if str(b.id) == book_id:
                return b

    def get_book_type(self, formatcode):
        """Get details about the given book format"""
        for bookType in self.book_types:
            if bookType.Format == formatcode:
                return bookType
            
    def add_book(self, b):
        """Add a book to the database"""
        existing_book = self.__get_book(b)
        if not existing_book:
            self.__books.append(b)
        else:
            existing_book.add_format(b.formats[0])
            
    def __get_book(self, book_to_get):
        for b in self.__books:
            if b == book_to_get:
                return b
