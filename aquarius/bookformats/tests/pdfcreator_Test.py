import unittest

from aquarius.bookformats.pdfcreator import PdfCreator
from aquarius.objects.Book import Book


class TestPdfCreator(unittest.TestCase):
    """Tests for the PdfCreator class"""

    def setUp(self):
        """Common setup operations."""
        self.__path = "aquarius/bookformats/tests/data/1.pdf"
        self.__p = PdfCreator()

    def testCallingCreateWithValidPathGivesABook(self):
        """Given a path to a .pdf file, when it exists on disk,
        an instance of the book object is created."""
        self.assertIsInstance(self.__p.create(self.__path), Book)

    def testCallingCreateGivesCorrectBookFormat(self):
        """Given a path to a .pdf file, when it exists on disk,
        the returned object has a format of PDF."""
        b = self.__p.create(self.__path)
        self.assertEquals("PDF", b.formats[0].Format)

    def testCallingCreateGivesCorrectBookLocation(self):
        """Given a path to a .pdf file, when it exists on disk,
        the returned object has the given location on disk."""
        b = self.__p.create(self.__path)
        self.assertEquals(self.__path, b.formats[0].Location)
