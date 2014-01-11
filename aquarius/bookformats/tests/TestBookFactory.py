import os
import shutil
import unittest

from aquarius.bookformats.BookFactory import BookFactory
from aquarius.bookformats.tests.epubcreatorspy import EpubCreatorSpy
from aquarius.objects.book import book


class TestBookFactory(unittest.TestCase):
    
    def setUp(self):
        self.__f = BookFactory()
        self.__epubPath = "aquarius/bookformats/tests/data/TreasureIsland.epub"
        self.__pdfpath = "aquarius/bookformats/tests/data/1.pdf"

    def testGetBookUnrecognisedGetsNoBook(self):
        b = self.__f.get_book("MyBook.rubbish")
        self.assertIsNone(b)

    def testGetEpubCausesCallToEpubCreatorCreate(self):
        spy = EpubCreatorSpy()
        self.__f.epub_creator = spy
        self.__f.get_book(self.__epubPath)
        self.assertTrue(spy.createcalled)

    def testGetPdfCausesCallToPdfCreatorCreate(self):
        spy = EpubCreatorSpy()
        self.__f.pdf_creator = spy
        self.__f.get_book(self.__pdfpath)
        self.assertTrue(spy.createcalled)
