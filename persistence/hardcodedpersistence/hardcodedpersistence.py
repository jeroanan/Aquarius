from objects.book import book

from persistence.hardcodedpersistence.setuptestbookhelper import setuptestbookhelper
from persistence.hardcodedpersistence.setuptestbooktypeshelper import setuptestbooktypeshelper

class hardcodedpersistence():    
    
    def __init__(self, config):
        self.__books = setuptestbookhelper().Setup()
        self.__booktypes = setuptestbooktypeshelper().Setup()   
        
    def SearchBooks(self, searchTerm):
        for book in self.__books:            
            if str.upper(searchTerm) in str.upper(book.Title) and searchTerm != "":                
                yield book
                
    def ListBooksByFirstLetter(self, firstLetter):
        for book in self.__books:
            if str.upper(book.Title).startswith(str.upper(firstLetter)):
                yield book
                
    def GetBookDetails(self, bookId): 
        for book in self.__books:      
            if str(book.Id) == bookId:
                return book

    def GetBookType(self, formatcode):
        for bookType in self.__booktypes:
            if bookType.Format == formatcode:
                return bookType
            
    def AddBook(self, book):
        bookExists = self.__BookExists(book)        
        if not bookExists:
            self.__books.append(book)
        else:
            self.__AddFormatToBook(book)
            
    def __BookExists(self, book):        
        for b in self.__books:
            if b.Author == book.Author and b.Title == book.Title:
                return True        
        return False
    
    def __AddFormatToBook(self, book):
        for b in self.__books:
            if b.Author == book.Author and b.Title == book.Title:
                b.Formats.append(book.Formats)
    
