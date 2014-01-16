"""Aquarius eBook management software"""
import os.path

from aquarius.bookharvesting.harvesterfactory import harvesterfactory
from aquarius.persistence.PersistenceFactory import PersistenceFactory
from aquarius.output.outputfactory import outputfactory
from config import config

workingDirectory = os.path.dirname(os.path.abspath(__file__))


class Aquarius(object):
    """The main class of the application. It initialises the application
        and is called back later for inter-module communication to take
        place"""
    def __init__(self, persistence_type, output_type, harvester_type):
        self.__config = config()
        self.__persistence = \
            PersistenceFactory(self.__config).get_persistence(persistence_type)
        self.__output = \
            outputfactory(self, self.__config).GetOutput(output_type)
        self.__harvester = \
            harvesterfactory(self, self.__config).GetHarvester(harvester_type)
        
    def main(self):
        """Passes control of execution to the output object"""
        self.__output.main()
              
    def SearchBooks(self, searchterm):
        """Executes the SearchBooks method on the persistence object"""
        return self.__persistence.SearchBooks(searchterm)
                        
    def ListBooksByFirstLetter(self, firstletter):
        """Executes the ListBooksByFirstLetter method
        on the persistence object"""
        return self.__persistence.ListBooksByFirstLetter(firstletter)
    
    def GetBookDetails(self, bookid):
        """Executes the GetBookDetails method on the persistence
        object"""
        return self.__persistence.GetBookDetails(bookid)
    
    def GetBookType(self, formatcode):
        """Executes the GetBookType method on the persistence object"""
        return self.__persistence.GetBookType(formatcode)
    
    def AddBook(self, book):
        """Executes the AddBook method on the persistence object"""
        self.__persistence.AddBook(book)
    
    def HarvestBooks(self):
        """Executes the DoHarvest method on the harvester object"""
        self.__harvester.doHarvest()

    def set_persistor(self, persistor):
        """Set the object used for persistence. For test use only.
        Not to be used in production."""
        pass