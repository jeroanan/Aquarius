import os
import unittest

from aquarius.Aquarius import Aquarius
from aquarius.bookharvesting.filesystemharvester import filesystemharvester
from config import config


class TestFileSystemHarvester(unittest.TestCase):
    """Tests for the FileSystemHarvester class"""
    def setUp(self):
        """Common setup operations"""
        self.__app = app()
        self.__config = config()
        self.__config.HarvestPaths = ["aquarius/bookformats/tests/data"]
        self.__h = filesystemharvester(self.__app, self.__config)
        self.__expected_number_of_books = 2

    def testHarvestSuccessful(self):
        """Given a harvest request, when the target directory contains only
        books, then the expected number of books are harvested."""
        self.__h.doHarvest()        
        self.assertEqual(self.__expected_number_of_books, len(self.__app.books))
        self.assertEqual("Treasure Island", self.__app.books[0].title)
        
    def testHarvestCruft(self):
        """Given a harvest request, when the target directory contains a
        non-book file, it's not harvested."""
        with open("aquarius/bookformats/tests/data/1.txt", "w") as f:
            pass
        self.__h.doHarvest()
        self.assertEqual(self.__expected_number_of_books, len(self.__app.books))
        os.remove("aquarius/bookformats/tests/data/1.txt")


class app(Aquarius):
    
    def __init__(self):
        self.books = []
    
    def AddBook(self, book):
        self.books.append(book)