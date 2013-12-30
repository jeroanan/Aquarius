from aquarius.objects.book import book
from aquarius.persistence.hardcodedpersistence.setuptestbookhelper import setuptestbookhelper
from aquarius.persistence.hardcodedpersistence.setuptestbooktypeshelper import setuptestbooktypeshelper

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
        existingBook = self.__GetBook(book)        
        if not existingBook:
            self.__books.append(book)
        else:
            existingBook.AddFormat(book.Formats[0])
            
    def __GetBook(self, book):        
        for b in self.__books:
            if b == book:
                return b
    