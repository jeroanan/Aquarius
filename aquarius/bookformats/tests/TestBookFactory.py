import unittest
from unittest.mock import Mock

from aquarius.bookformats.BookFactory import BookFactory
from aquarius.bookformats.epubcreator import EpubCreator
from aquarius.bookformats.pdfcreator import PdfCreator


class TestBookFactory(unittest.TestCase):

    def setUp(self):
        self.__f = BookFactory()
        self.__epubPath = "aquarius/bookformats/tests/data/TreasureIsland.epub"
        self.__pdfpath = "aquarius/bookformats/tests/data/1.pdf"

    def testGetBookUnrecognisedGetsNoBook(self):
        b = self.__f.get_book("MyBook.rubbish")
        self.assertIsNone(b)

    def testGetEpubCausesCallToEpubCreatorCreate(self):
        epub_creator = EpubCreator()
        epub_creator.create = Mock()
        self.__f.epub_creator = epub_creator
        self.__f.get_book(self.__epubPath)
        self.assertTrue(epub_creator.create.called)

    def testGetPdfCausesCallToPdfCreatorCreate(self):
        pdf_creator = PdfCreator()
        pdf_creator.create = Mock()
        self.__f.pdf_creator = pdf_creator
        self.__f.get_book(self.__pdfpath)
        self.assertTrue(pdf_creator.create.called)

    def test_epub_creator_property(self):
        self.__f.epub_creator = "moo"
        self.assertEquals("moo", self.__f.epub_creator)

    def test_pdf_creator_property(self):
        self.__f.pdf_creator = "moo"
        self.assertEquals("moo", self.__f.pdf_creator)
