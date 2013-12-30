import os
import unittest

from aquarius.aquarius import aquarius
from aquarius.bookharvesting.filesystemharvester import filesystemharvester
from config import config

class filesystemharvester_tests(unittest.TestCase):
    
    def setUp(self):
        self.__app = app()
        self.__config = config()
        self.__config.HarvestPaths = ["aquarius/bookformats/tests/data"]
        self.__h = filesystemharvester(self.__app, self.__config)
        
    def testHarvestSuccessful(self):
        self.__h.doHarvest()        
        self.assertEqual(1, len(self.__app.books))
        self.assertEqual("Treasure Island", self.__app.books[0].Title)
        
    def testHarvestCruft(self):
        with open("aquarius/bookformats/tests/data/1.txt", "w") as f:
            pass
        
        self.__h.doHarvest()
        self.assertEqual(1, len(self.__app.books))
        os.remove("aquarius/bookformats/tests/data/1.txt")
        
class app(aquarius):
    
    def __init__(self):
        self.books = []
    
    def AddBook(self, book):
        self.books.append(book)