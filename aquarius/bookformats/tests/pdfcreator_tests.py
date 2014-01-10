import unittest

from aquarius.bookformats.pdfcreator import PdfCreator
from aquarius.objects.book import book


class PdfCreator_tests(unittest.TestCase):

    def setUp(self):
        self.__path = "aquarius/bookformats/tests/data/1.pdf"
        self.__p = PdfCreator()

    def testCallingCreateWithAnInvalidPathGivesNone(self):
        self.assertIsNone(self.__p.create("/does/not/exist"))

    def testCallingCreateWithValidPathGivesABook(self):
        self.assertIsInstance(self.__p.create(self.__path), book)

    def testCallingCreateGivesCorrectBookFormat(self):
        b = self.__p.create(self.__path)
        self.assertEquals("PDF", b.Formats[0].Format)

    def testCallingCreateGivesCorrectBookLocation(self):
        b = self.__p.create(self.__path)
        self.assertEquals(self.__path, b.Formats[0].Location)