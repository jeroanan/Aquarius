import unittest

from aquarius.Aquarius import Aquarius
from aquarius.bookharvesting.FileSystemHarvester import FileSystemHarvester
from Config import Config


class TestFileSystemHarvester(unittest.TestCase):
    """Tests for the FileSystemHarvester class"""
    def setUp(self):
        """Common setup operations"""
        self.__app = App()
        self.__config = Config()
        self.__config.harvest_paths = ["aquarius/bookformats/tests/data"]
        self.__h = FileSystemHarvester(self.__app, self.__config)
        self.__expected_number_of_books = 2


class App(Aquarius):

    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)