#!/usr/bin/python3

from persistence.persistencefactory import persistencefactory
from output.outputfactory import outputfactory

class aquarius(object):    
        
    def __init__(self, persistencetype, outputtype):
        self.__persistence = persistencefactory().GetPersistence(persistencetype)        
        self.__output = outputfactory(self).GetOutput(outputtype)
    
    def Main(self):
        self.__output.Main()
              
    def SearchBooks(self, searchTerm, callback):
        callback(self.__persistence.SearchBooks(searchTerm))
                
    def ListBooksByFirstLetter(self, firstLetter, callback):
        callback(self.__persistence.ListBooksByFirstLetter(firstLetter))
    
    def GetBookDetails(self, bookId, callback):
        callback(self.__persistence.GetBookDetails(bookId))
    
    def GetBook(self, bookId, callback):
        callback(self.__persistence.GetBook(bookId))
    