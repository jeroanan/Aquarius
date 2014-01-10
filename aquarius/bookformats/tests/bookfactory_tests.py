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
        self.__pdfpath = "aquarius/bookformats/tests/data/1.pdf"

    def testGetBookUnrecognisedGetsNoBook(self):
        b = self.__f.GetBook("MyBook.rubbish")
        self.assertIsNone(b)

    def testHasEpubCreatorAttribute(self):
        self.assertTrue(hasattr(self.__f, "EpubCreator"))

    def testHasPdfCreatorAttribute(self):
        self.assertTrue(hasattr(self.__f, "PdfCreator"))

    def testGetEpubCausesCallToEpubCreatorCreate(self):
        spy = EpubCreatorSpy()
        self.__f.EpubCreator = spy
        self.__f.GetBook(self.__epubPath)
        self.assertTrue(spy.createcalled)

    def testGetPdfCausesCallToPdfCreatorCreate(self):
        spy = EpubCreatorSpy()
        self.__f.PdfCreator = spy
        self.__f.GetBook(self.__pdfpath)
        self.assertTrue(spy.createcalled)
