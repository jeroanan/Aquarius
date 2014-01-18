from aquarius.objects.book import book
from aquarius.persistence.hardcodedpersistence.SetupTestBookHelper import SetupTestBookHelper
from aquarius.persistence.hardcodedpersistence.SetupTestBookTypesHelper import SetupTestBookTypesHelper


class HardcodedPersistence(object):
    """Provides a hardcoded datastore. It implements the same interface as the
     other persistors but any data added to/removed from it is transient and
     forgotten between sessions, as it's all stored in memory"""

    def __init__(self, config):
        self.__books = SetupTestBookHelper().Setup()
        self.book_types = SetupTestBookTypesHelper().Setup()
        
    def search_books(self, search_term):
        """Searches for books in the database, returning a result set as a list
        of book objects"""
        for b in self.__books:
            if str.upper(search_term) in \
                    str.upper(b.Title) and search_term != "":
                yield b

    def list_books_by_first_letter(self, first_letter):
        """Searches for books whose title begins with the given letter,
        returning a result set as a list of book objects"""
        for b in self.__books:
            if str.upper(b.Title).startswith(str.upper(first_letter)):
                yield b
                
    def get_book_details(self, book_id):
        """Gets a given book by Id. Returns a book object."""
        for b in self.__books:
            if str(b.Id) == book_id:
                return b

    def GetBookType(self, formatcode):
        """Get details about the given book format"""
        for bookType in self.book_types:
            if bookType.Format == formatcode:
                return bookType
            
    def AddBook(self, book):
        """Add a book to the database"""
        existingBook = self.__get_book(book)
        if not existingBook:
            self.__books.append(book)
        else:
            existingBook.AddFormat(book.Formats[0])
            
    def __get_book(self, book):
        for b in self.__books:
            if b == book:
                return b
