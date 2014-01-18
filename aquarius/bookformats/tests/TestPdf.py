import unittest

from aquarius.bookformats.Pdf import Pdf
from aquarius.bookformats.tests.pdfreaderspy import PdfReaderSpy


class TestPdf(unittest.TestCase):
    """Tests for the Pdf class"""
    def setUp(self):
        """Common setup operations"""
        self.__p = Pdf("aquarius/bookformats/tests/data/1.pdf")

    def testCallingLoadCallsPdfReaderGetDocumentInfo(self):
        """Given a book, when the load method is called,
        then the PdfReader's get_document_info method is called."""
        spy = PdfReaderSpy(None)
        self.__p.set_pdf_reader(spy)
        self.__p.load()
        self.assertTrue(spy.get_document_info_called)

    def testCallingLoadSetsCorrectAuthor(self):
        """Given a book, when the load method is called,
        then the returned book's author is correctly set."""
        self.__p.load()
        self.assertEquals("Robert Louis Stevenson", self.__p.author)

    def testCallingLoadSetsCorrectTitle(self):
        """Given a book, when the load method is called,
        then the returned book's title is correctly set."""
        self.__p.load()
        self.assertEquals("Treasure Island", self.__p.title)