#!/usr/bin/python3

from persistence.persistencefactory import persistencefactory

class aquarius(object):    
        
    def __init__(self, persistortype):
        self.__persistence = persistencefactory().GetPersistence(persistortype)        
    
    def SearchBooks(self, searchTerm, callback):
        callback(self.__persistence.SearchBooks(searchTerm))
                
    def ListBooksByFirstLetter(self, firstLetter, callback):
        callback(self.__persistence.ListBooksByFirstLetter(firstLetter))
    
    def GetBookDetails(self, bookId, callback):
        callback(self.__persistence.GetBookDetails(bookId))
    
    def GetBook(self, bookId, callback):
        callback(self.__persistence.GetBook(bookId))
    