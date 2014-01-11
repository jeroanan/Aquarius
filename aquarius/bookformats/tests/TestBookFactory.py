import os
import shutil
import unittest

from aquarius.bookformats.BookFactory import BookFactory
from aquarius.bookformats.tests.epubcreatorspy import EpubCreatorSpy
from aquarius.objects.book import book


class TestBookFactory(unittest.TestCase):
    """Unit tests for the BookFactory class"""
    def setUp(self):
        """Common setup operations"""
        self.__f = BookFactory()
        self.__epubPath = "aquarius/bookformats/tests/data/TreasureIsland.epub"
        self.__pdfpath = "aquarius/bookformats/tests/data/1.pdf"

    def testGetBookUnrecognisedGetsNoBook(self):
        """Given a filename, when the factory does not recognise its file
        extension, then return null"""
        b = self.__f.get_book("MyBook.rubbish")
        self.assertIsNone(b)

    def testGetEpubCausesCallToEpubCreatorCreate(self):
        """Given a filename, when it is a .epub file, then call the epub
        creator's create method"""
        spy = EpubCreatorSpy()
        self.__f.epub_creator = spy
        self.__f.get_book(self.__epubPath)
        self.assertTrue(spy.createcalled)

    def testGetPdfCausesCallToPdfCreatorCreate(self):
        """Given a filename, when it is a .pdf file, then call the pdf
        creator's create method"""
        spy = EpubCreatorSpy()
        self.__f.pdf_creator = spy
        self.__f.get_book(self.__pdfpath)
        self.assertTrue(spy.createcalled)
