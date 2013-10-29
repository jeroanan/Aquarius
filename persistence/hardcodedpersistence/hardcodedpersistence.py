from objects.book import book
from objects.booktype import booktype

from persistence.hardcodedpersistence.setuptestbookhelper import setuptestbookhelper


class hardcodedpersistence():    
    
    def __init__(self):
        self.__data = setuptestbookhelper().Setup()
        self.__booktypes = []
        
        self.__SetupBookTypes()
            
    def __SetupBookTypes(self):
        self.__SetupEpubBookType()
        self.__SetupMobiBookType()
        self.__SetupPdfBookType()
        
    def __SetupEpubBookType(self):
        epub = booktype()
        epub.Format = "EPUB"
        epub.MimeType = "application/epub+zip"
        self.__booktypes.append(epub)
        
    def __SetupMobiBookType(self):
        mobi = booktype()
        mobi.Format = "MOBI"
        mobi.MimeType = "application/x-mobipocket-ebook"
        self.__booktypes.append(mobi)
        
    def __SetupPdfBookType(self):
        pdf = booktype()
        pdf.Format = "PDF"
        pdf.MimeType = "application/x-pdf"
        self.__booktypes.append(pdf)
        
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
            