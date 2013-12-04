import os
import unittest
import aquarius
from bookharvesting.filesystemharvester import filesystemharvester

class filesystemharvester_tests(unittest.TestCase):
    
    def setUp(self):
        self.__app = app()
        self.__h = filesystemharvester(self.__app)       
    
    def testHarvestSuccessful(self):
        self.__h.doHarvest("bookformats/tests/data/")
        self.assertEqual(1, len(self.__app.books))
        self.assertEqual("Treasure Island", self.__app.books[0].Title)
        
    def testHarvestCruft(self):
        with open("bookformats/tests/data/1.txt", "w") as f:
            pass
        
        self.__h.doHarvest("bookformats/tests/data/")
        self.assertEqual(1, len(self.__app.books))
        os.remove("bookformats/tests/data/1.txt")
        
class app(aquarius.aquarius):
    
    def __init__(self):
        self.books = []
    
    def AddBook(self, book):
        self.books.append(book)