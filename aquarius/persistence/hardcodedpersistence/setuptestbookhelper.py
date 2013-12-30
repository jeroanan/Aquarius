from objects.book import book
from objects.bookformat import bookformat

import os

class setuptestbookhelper(object):
       
    def __init__(self):
        self.__books = []
        
    def Setup(self):
        self.__books.append(self.__AddBookWithAllFormats())
        self.__books.append(self.__AddBookWithNoFormats())        
        return self.__books

    def __AddBookWithAllFormats(self):
        b = book()
        b.Id = 1
        b.Title = "The Book with no name"
        b.Author = "An Author"
        b.AuthorUri = "about:none"        
        b.Formats.append(self.__getEpubFormat())
        b.Formats.append(self.__getMobiFormat())
        b.Formats.append(self.__getPdfFormat())
        return b
    
    def __AddBookWithNoFormats(self):
        b = book()
        b.Id = 1
        b.Title = "Treasure Island"
        b.Author = "Robert Louis Stevenson"
        b.AuthorUri = "about:none"
        return b
    
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



