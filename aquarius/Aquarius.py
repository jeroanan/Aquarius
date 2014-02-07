"""Aquarius eBook management software"""
import os.path

from aquarius.bookharvesting.HarvesterFactory import HarvesterFactory
from aquarius.persistence.PersistenceFactory import PersistenceFactory
from aquarius.output.OutputFactory import OutputFactory
from Config import Config

WorkingDirectory = os.path.dirname(os.path.abspath(__file__))


class Aquarius(object):

    """The main class of the application. It initialises the application
        and is called back later for inter-module communication to take
        place"""
    def __init__(self, persistence_type, output_type, harvester_type):
        self.__is_harvesting = False
        self.__config = Config()
        self.__persistence = \
            PersistenceFactory(self.__config).get_persistence(persistence_type)
        self.__output = \
            OutputFactory(self, self.__config).get_output(output_type)
        self.__harvester = \
            HarvesterFactory(self, self.__config).get_harvester(harvester_type)

    def main(self):
        """Passes control of execution to the output object"""
        self.__output.main()
              
    def search_books(self, searchterm):
        """Executes the SearchBooks method on the persistence object"""
        return self.__persistence.search_books(searchterm)
                        
    def list_books_by_first_letter(self, firstletter):
        """Executes the ListBooksByFirstLetter method
        on the persistence object"""
        return self.__persistence.list_books_by_first_letter(firstletter)
    
    def get_book_details(self, bookid):
        """Executes the GetBookDetails method on the persistence
        object"""
        return self.__persistence.get_book_details(bookid)
    
    def get_book_type(self, formatcode):
        """Executes the GetBookType method on the persistence object"""
        return self.__persistence.get_book_type(formatcode)
    
    def add_book(self, book):
        """Executes the AddBook method on the persistence object"""
        self.__persistence.add_book(book)
    
    def harvest_books(self):
        """Executes the DoHarvest method on the harvester object"""
        self.__harvester.do_harvest()

    def set_persistor(self, persistor):
        """Set the object used for persistence. For test use only.
        Not to be used in production."""
        pass

    @property
    def is_harvesting(self):
        return self.__is_harvesting

    @is_harvesting.setter
    def is_harvesting(self, val):
        self.__is_harvesting = val