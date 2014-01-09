import os
import shutil
import unittest

from aquarius.bookformats.bookfactory import bookfactory
from aquarius.bookformats.tests.epubcreatorspy import EpubCreatorSpy
from aquarius.objects.book import book


class bookfactory_tests(unittest.TestCase):
    
    def setUp(self):
        self.__f = bookfactory()
        self.__epubPath = "aquarius/bookformats/tests/data/TreasureIsland.epub"
        self.__UcaseEpubPath = "aquarius/bookformats/tests/data/TreasureIsland.EPUB"
        shutil.copy(self.__epubPath, self.__UcaseEpubPath)
        
    def tearDown(self):
        os.remove(self.__UcaseEpubPath)
        
    @unittest.skip
    def testGetBookEpubGetsBookUpperCase(self):
        self.assertIsInstance(self.__f.GetBook(self.__UcaseEpubPath), book)

    def testGetBookUnrecognisedGetsNoBook(self):
        b = self.__f.GetBook("MyBook.rubbish")
        self.assertIsNone(b)

    def testHasEpubCreatorAttribute(self):
        self.assertTrue(hasattr(self.__f, "EpubCreator"))

    def testGetEpubCausesCallToEpubCreatorCreate(self):
        spy = EpubCreatorSpy()
        self.__f.EpubCreator = spy
        self.__f.GetBook(self.__epubPath)
        self.assertTrue(spy.createcalled)