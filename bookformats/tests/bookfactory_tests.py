import os
import shutil
import unittest
from bookformats.bookfactory import bookfactory
from objects.book import book

class bookfactory_tests(unittest.TestCase):
    
    def setUp(self):
        self.__f = bookfactory()
        shutil.copy("bookformats/tests/data/TreasureIsland.epub", "bookformats/tests/data/TreasureIsland.EPUB")
        
    def tearDown(self):
        os.remove("bookformats/tests/data/TreasureIsland.EPUB")
        
    def testGetBookEpubGetsBook(self):
        b = self.__f.GetBook("bookformats/tests/data/TreasureIsland.epub")
        self.assertIsInstance(b, book)       
    
    def testGetBookEpubGetsBookUpperCase(self):
        b = self.__f.GetBook("bookformats/tests/data/TreasureIsland.EPUB")
        self.assertIsInstance(b, book)
    
    def testGetIndalidEpub(self):
        b = self.__f.GetBook("bookformats/tests/data/NotAValidEpub.epub")
        self.assertIsNone(b)
        
    def testGetBookUnrecognisedGetsNoBook(self):
        b = self.__f.GetBook("MyBook.rubbish")
        self.assertIsNone(b)
        
    