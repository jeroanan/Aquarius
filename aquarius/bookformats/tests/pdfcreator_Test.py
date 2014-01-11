import unittest

from aquarius.bookformats.pdfcreator import PdfCreator
from aquarius.objects.book import book


class TestPdfCreator(unittest.TestCase):
    """Tests for the PdfCreator class"""

    def setUp(self):
        """Common setup operations."""
        self.__path = "aquarius/bookformats/tests/data/1.pdf"
        self.__p = PdfCreator()

    def testCallingCreateWithValidPathGivesABook(self):
        """Given a path to a .pdf file, when it exists on disk,
        an instance of the book object is created."""
        self.assertIsInstance(self.__p.create(self.__path), book)

    def testCallingCreateGivesCorrectBookFormat(self):
        """Given a path to a .pdf file, when it exists on disk,
        the returned object has a format of PDF."""
        b = self.__p.create(self.__path)
        self.assertEquals("PDF", b.Formats[0].Format)

    def testCallingCreateGivesCorrectBookLocation(self):
        """Given a path to a .pdf file, when it exists on disk,
        the returned object has the given location on disk."""
        b = self.__p.create(self.__path)
        self.assertEquals(self.__path, b.Formats[0].Location)

    def testCallingCreateWithAnInvalidPathGivesNone(self):
        """Given a path to a .pdf file, when it doesn't exist on disk,
        the returned object is null."""
        self.assertIsNone(self.__p.create("/does/not/exist"))
