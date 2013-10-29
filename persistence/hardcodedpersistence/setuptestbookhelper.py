from objects.book import book
from objects.bookformat import bookformat

import os

class setuptestbookhelper(object):
       
    def __init__(self):
        self.__data = []
        
    def Setup(self):
        b = self.__AddBook()    
        b.Formats.append(self.__AddFormatDetails())  
              
        self.__data.append(b)        
        return self.__data

    def __AddBook(self):
        b = book()
        b.Title = "The Book with no name"
        b.Author = "An Author"
        b.Id = 1
        return b
    
    def __AddFormatDetails(self):
        f = bookformat()
        f.Format = "EPUB"
        f.Location = "%s/1.EPUB" % os.getcwd()
        return f

    
    



