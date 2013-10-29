from objects.book import book
from objects.bookformat import bookformat
from objects.booktype import booktype

import os

class hardcodedpersistence():    
    
    def __init__(self):
        self.__data = []
        self.__booktypes = []
        
        self.SetupTestBook()        
        self.SetupBookTypes()       
        
    def SetupTestBook(self):        
        b = book()        
        b.Title = "The Book with no name"
        b.Id = 1    

        f = bookformat()
        f.Format = "EPUB"
        f.Location = "%s/1.EPUB" % os.getcwd()
        b.Formats.append(f)        
        self.__data.append(b)
        
    def SetupBookTypes(self):
        self.SetupEpubBookType()
        self.SetupMobiBookType()
        self.SetupPdfBookType()
        
    def SetupEpubBookType(self):
        epub = booktype()
        epub.Format = "EPUB"
        epub.MimeType = "application/epub+zip"
        self.__booktypes.append(epub)
        
    def SetupMobiBookType(self):
        mobi = booktype()
        mobi.Format = "MOBI"
        mobi.MimeType = "application/x-mobipocket-ebook"
        self.__booktypes.append(mobi)
        
    def SetupPdfBookType(self):
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
            