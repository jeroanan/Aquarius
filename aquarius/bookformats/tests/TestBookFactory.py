import unittest

from aquarius.bookformats.BookFactory import BookFactory
from aquarius.bookformats.tests.epubcreatorspy import EpubCreatorSpy


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

    def test_epub_creator_property(self):
        self.__f.epub_creator = "moo"
        self.assertEquals("moo", self.__f.epub_creator)

    def test_pdf_creator_property(self):
        self.__f.pdf_creator = "moo"
        self.assertEquals("moo", self.__f.pdf_creator)
