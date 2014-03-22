import unittest

from aquarius.bookformats.Pdf import Pdf
from tests.bookformats.pdfreaderspy import PdfReaderSpy


class TestPdf(unittest.TestCase):

    def setUp(self):
        self.__p = Pdf("tests/data/1.pdf")

    def test_load_calls_pdf_reader_get_document_info(self):
        pdf_reader = PdfReaderSpy(None)
        self.__p.set_pdf_reader(pdf_reader)
        self.__p.load()
        self.assertTrue(pdf_reader.get_document_info_called)

    def test_load_sets_correct_author(self):
        self.__p.load()
        self.assertEquals("Robert Louis Stevenson", self.__p.author)

    def test_load_sets_correct_title(self):
        self.__p.load()
        self.assertEquals("Treasure Island", self.__p.title)