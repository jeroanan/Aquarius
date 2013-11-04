from objects.book import book

from persistence.hardcodedpersistence.setuptestbookhelper import setuptestbookhelper
from persistence.hardcodedpersistence.setuptestbooktypeshelper import setuptestbooktypeshelper

class hardcodedpersistence():    
    
    def __init__(self, config):
        self.__data = setuptestbookhelper().Setup()
        self.__booktypes = setuptestbooktypeshelper().Setup()   
        
    def SearchBooks(self, searchTerm):
        for book in self.__data:
            if str.upper(searchTerm) in str.upper(book.Title) and searchTerm != "":
                yield book
                
    def ListBooksByFirstLetter(self, firstLetter):
        for book in self.__data:
            if str.upper(book.Title).startswith(str.upper(firstLetter)):
                yield book
                
    def GetBookDetails(self, bookId): 
        for book in self.__data:      
            if str(book.Id) == bookId:
                return book

    def GetBookType(self, formatcode):
        for bookType in self.__booktypes:
            if bookType.Format == formatcode:
                return bookType
            