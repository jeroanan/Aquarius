#!/usr/bin/python3

from persistence.persistencefactory import persistencefactory

class aquarius(object):    
        
    def __init__(self, persistortype):
        self.__persistor = persistencefactory().GetPersistor(persistortype)        
    
    def SearchBooks(self, searchTerm):
        return self.__persistor.SearchBooks(searchTerm)
                
    def ListBooksByFirstLetter(self, firstLetter):
        return self.__persistor.ListBooksByFirstLetter(firstLetter)
    
    def GetBookDetails(self, bookId):
        return self.__persistor.GetBookDetails(bookId)
    
    def GetBook(self, bookId):
        pass
    