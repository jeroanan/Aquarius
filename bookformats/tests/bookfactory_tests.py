import unittest
from bookformats.bookfactory import bookfactory
from objects.book import book

class bookfactory_tests(unittest.TestCase):
    
    def setUp(self):
        self.__f = bookfactory()
        
    def testGetBookEpubGetsBook(self):
        b = self.__f.GetBook("bookformats/tests/data/TreasureIsland.epub")
        self.assertIsInstance(b, book)       
    
    def testGetBookUnrecognisedGetsNoBook(self):
        b = self.__f.GetBook("MyBook.rubbish")
        self.assertIsNone(b)