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
    def __init__(self, persistence_type, output_type, harvester_type, interactor_factory):
        self.__is_harvesting = False
        self.__config = Config()
        self.__persistence = \
            PersistenceFactory(self.__config).get_persistence(persistence_type)
        self.__output = \
            OutputFactory(self, self.__config).get_output(output_type)
        self.__harvester = \
            HarvesterFactory(self, self.__config).get_harvester(harvester_type)
        self.__interactor_factory = interactor_factory

    def main(self):
        self.__output.main()
              
    def search_books(self, search_term):
        i = self.__interactor_factory.get_search_book_interactor(self.__persistence)
        return i.execute(search_term)
                        
    def list_books_by_first_letter(self, first_letter):
        i = self.__interactor_factory.get_list_books_by_first_letter_interactor(self.__persistence)
        return i.execute(first_letter)
    
    def get_book_details(self, book_id):
        i = self.__interactor_factory.get_book_details_interactor(self.__persistence)
        return i.execute(book_id)
    
    def get_book_type(self, format_code):
        return self.__persistence.get_book_type(format_code)
    
    def add_book(self, book):
        i = self.__interactor_factory.get_add_book_interactor(self.__persistence)
        i.execute(book)
    
    def harvest_books(self):
        if not self.is_harvesting:
            self.__harvester.do_harvest()

    @property
    def is_harvesting(self):
        return self.__is_harvesting

    @is_harvesting.setter
    def is_harvesting(self, val):
        self.__is_harvesting = val

    def set_persistence(self, persistence):
        self.__persistence = persistence

    def set_output(self, output):
        self.__output = output

    def set_harvester(self, harvester):
        self.__harvester = harvester
