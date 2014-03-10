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
        self.__output.main()
              
    def search_books(self, search_term):
        return self.__persistence.search_books(search_term)
                        
    def list_books_by_first_letter(self, first_letter):
        return self.__persistence.list_books_by_first_letter(first_letter)
    
    def get_book_details(self, book_id):
        return self.__persistence.get_book_details(book_id)
    
    def get_book_type(self, format_code):
        return self.__persistence.get_book_type(format_code)
    
    def add_book(self, book):
        self.__persistence.add_book(book)
    
    def harvest_books(self):
        if not self.is_harvesting:
            self.__harvester.do_harvest()

    def set_persistor(self, persistor):
        pass

    @property
    def is_harvesting(self):
        return self.__is_harvesting

    @is_harvesting.setter
    def is_harvesting(self, val):
        self.__is_harvesting = val

    def set_harvester(self, harvester):
        self.__harvester = harvester