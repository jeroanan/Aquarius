#!/usr/bin/python3

from persistence.persistencefactory import persistencefactory

class aquarius(object):    
        
    def __init__(self, persistortype):
        self.__persistence = persistencefactory().GetPersistence(persistortype)        
    
    def SearchBooks(self, searchTerm):
        return self.__persistence.SearchBooks(searchTerm)
                
    def ListBooksByFirstLetter(self, firstLetter):
        return self.__persistence.ListBooksByFirstLetter(firstLetter)
    
    def GetBookDetails(self, bookId):
        return self.__persistence.GetBookDetails(bookId)
    
    def GetBook(self, bookId):
        return self.__persistence.GetBook(bookId)
    