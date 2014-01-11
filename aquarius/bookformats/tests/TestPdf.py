import unittest

from aquarius.bookformats.Pdf import Pdf
from aquarius.bookformats.tests.pdfreaderspy import PdfReaderSpy


class TestPdf(unittest.TestCase):

    def setUp(self):
        self.__p = Pdf("aquarius/bookformats/tests/data/1.pdf")

    def testCanSetPdfFileReaderClass(self):
        self.__p.set_pdf_reader(None)

    def testCallingLoadCallsPdfReaderGetDocumentInfo(self):
        spy = PdfReaderSpy(None)
        self.__p.set_pdf_reader(spy)
        self.__p.load()
        self.assertTrue(spy.get_document_info_called)

    def testCallingLoadSetsCorrectAuthor(self):
        self.__p.load()
        self.assertEquals("Robert Louis Stevenson", self.__p.author)

    def testCallingLoadSetsCorrectTitle(self):
        self.__p.load()
        self.assertEquals("Treasure Island", self.__p.Title)