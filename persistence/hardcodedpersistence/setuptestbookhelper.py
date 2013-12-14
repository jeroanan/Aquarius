from objects.book import book
from objects.bookformat import bookformat

import os

class setuptestbookhelper(object):
       
    def __init__(self):
        self.__books = []
        
    def Setup(self):
        b = self.__AddBook()    
        b.Formats = self.__AddFormatDetails()                
        self.__books.append(b)        
        return self.__books

    def __AddBook(self):
        b = book()
        b.Title = "The Book with no name"
        b.Author = "An Author"
        b.AuthorUri = "about:none"
        b.Id = 1
        return b
    
    def __AddFormatDetails(self):
        result = []
        result.append(self.__getEpubFormat())
        result.append(self.__getMobiFormat())
        result.append(self.__getPdfFormat())
        return result
    
    def __getEpubFormat(self):
        return self.__getFormat("EPUB")

    def __getMobiFormat(self):
        return self.__getFormat("MOBI")
    
    def __getPdfFormat(self):
        return self.__getFormat("PDF")
    
    def __getFormat(self, formatCode):
        f = bookformat()
        f.Format = formatCode
        f.Location = "%s/1.%s" % (os.getcwd(), formatCode)
        return f



