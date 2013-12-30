import os
import shutil
import unittest

from aquarius.bookformats.bookfactory import bookfactory
from aquarius.objects.book import book

class bookfactory_tests(unittest.TestCase):
    
    def setUp(self):
        self.__f = bookfactory()
        self.__treasureIslandPath = "aquarius/bookformats/tests/data/TreasureIsland.epub"
        self.__treasureIslandUcasePath = "aquarius/bookformats/tests/data/TreasureIsland.EPUB"
        shutil.copy(self.__treasureIslandPath, self.__treasureIslandUcasePath)
        
    def tearDown(self):
        os.remove(self.__treasureIslandUcasePath)
        
    def testGetBookEpubGetsBook(self):
        self.assertIsInstance(self.__getTreasureIsland(), book)       
    
    def testGetBookEpubGetsBookUpperCase(self):
        self.assertIsInstance(self.__f.GetBook(self.__treasureIslandUcasePath), book)
    
    def testGetBookEpubGetsCorrectFormatName(self):
        b = self.__getTreasureIsland()
        self.assertEquals("EPUB", b.Formats[0].Format)
    
    def testGetBookEpubGetsCorrectLocation(self):
        b = self.__getTreasureIsland()
        self.assertEquals(self.__treasureIslandPath, b.Formats[0].Location)
        
    def testGetInvalidEpub(self):
        b = self.__f.GetBook("bookformats/tests/data/NotAValidEpub.epub")
        self.assertIsNone(b)
        
    def testGetBookUnrecognisedGetsNoBook(self):
        b = self.__f.GetBook("MyBook.rubbish")
        self.assertIsNone(b)
        
    def __getTreasureIsland(self):
        return self.__f.GetBook(self.__treasureIslandPath)