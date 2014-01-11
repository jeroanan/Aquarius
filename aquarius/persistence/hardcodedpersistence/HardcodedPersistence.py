from aquarius.objects.book import book
from aquarius.persistence.hardcodedpersistence.SetupTestBookHelper import SetupTestBookHelper
from aquarius.persistence.hardcodedpersistence.SetupTestBookTypesHelper import SetupTestBookTypesHelper


class HardcodedPersistence():
    """Provides a hardcoded datastore. It implements the same interface as the
     other persistors but any data added to/removed from it is transient and
     forgotten between sessions, as it's all stored in memory"""

    def __init__(self, config):
        self.__books = SetupTestBookHelper().Setup()
        self.__booktypes = SetupTestBookTypesHelper().Setup()
        
    def SearchBooks(self, searchTerm):
        """Searches for books in the database, returning a result set as a list
        of book objects"""
        for book in self.__books:            
            if str.upper(searchTerm) in str.upper(book.Title) and searchTerm != "":
                yield book
                
    def ListBooksByFirstLetter(self, firstLetter):
        """Searches for books whose title begins with the given letter,
        returning a result set as a list of book objects"""
        for book in self.__books:
            if str.upper(book.Title).startswith(str.upper(firstLetter)):
                yield book
                
    def GetBookDetails(self, bookId):
        """Gets a given book by Id. Returns a book object."""
        for book in self.__books:      
            if str(book.Id) == bookId:
                return book

    def GetBookType(self, formatcode):
        """Get details about the given book format"""
        for bookType in self.__booktypes:
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
