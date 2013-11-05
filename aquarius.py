#!/usr/bin/python3

from bookharvesting.harvesterfactory import harvesterfactory
from persistence.persistencefactory import persistencefactory
from output.outputfactory import outputfactory
from config import config

class aquarius(object):    
        
    def __init__(self, persistencetype, outputtype):
        self.__config = config()
        self.__persistence = persistencefactory(self.__config).GetPersistence(persistencetype)        
        self.__output = outputfactory(self, self.__config).GetOutput(outputtype) 
        self.__harvester = harvesterfactory(self).GetHarvester()       
        
    def Main(self):
        self.__output.Main()
              
    def SearchBooks(self, searchTerm):
        return self.__persistence.SearchBooks(searchTerm)
                        
    def ListBooksByFirstLetter(self, firstLetter):
        return self.__persistence.ListBooksByFirstLetter(firstLetter)
    
    def GetBookDetails(self, bookId):
        return self.__persistence.GetBookDetails(bookId)
    
    def GetBookType(self, formatcode):
        return self.__persistence.GetBookType(formatcode)
    
    def AddBook(self, book):
        pass
    
    def HarvestBooks(self):
        pass
    
    
    
    
    
    