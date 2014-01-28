import unittest

from aquarius.bookformats.pdfcreator import PdfCreator
from aquarius.objects.Book import Book


class TestPdfCreator(unittest.TestCase):

    def setUp(self):
        self.__path = "aquarius/bookformats/tests/data/1.pdf"
        self.__p = PdfCreator()

    def testCallingWithInvalidPathGivesNone(self):
        self.assertIsNone(self.__p.create("/tmp/1.pdf"))

    def testCallingCreateWithValidPathGivesABook(self):
        self.assertIsInstance(self.__p.create(self.__path), Book)

    def testCallingCreateGivesCorrectBookFormat(self):
        b = self.__p.create(self.__path)
        self.assertEquals("PDF", b.formats[0].Format)

    def testCallingCreateGivesCorrectBookLocation(self):
        b = self.__p.create(self.__path)
        self.assertEquals(self.__path, b.formats[0].Location)
