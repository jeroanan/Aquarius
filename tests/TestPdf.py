import unittest
from unittest.mock import Mock
from PyPDF2 import PdfFileReader

from aquarius.bookformats.Pdf import Pdf
from aquarius.bookformats.tests.pdfreaderspy import PdfReaderSpy


class TestPdf(unittest.TestCase):

    def setUp(self):
        self.__p = Pdf("aquarius/bookformats/tests/data/1.pdf")

    def testCallingLoadCallsPdfReaderGetDocumentInfo(self):
        pdf_reader = PdfReaderSpy(None)
        self.__p.set_pdf_reader(pdf_reader)
        self.__p.load()
        self.assertTrue(pdf_reader.get_document_info_called)

    def testCallingLoadSetsCorrectAuthor(self):
        self.__p.load()
        self.assertEquals("Robert Louis Stevenson", self.__p.author)

    def testCallingLoadSetsCorrectTitle(self):
        self.__p.load()
        self.assertEquals("Treasure Island", self.__p.title)