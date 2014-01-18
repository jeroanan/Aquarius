import unittest

from aquarius.bookformats.epubcreator import EpubCreator
from aquarius.objects.Book import Book


class TestEpubCreator(unittest.TestCase):
    """Tests for the EpubCreator class"""
    def setUp(self):
        """Common setup operations."""
        self.__epubPath = "aquarius/bookformats/tests/data/TreasureIsland.epub"
        self.__epc = EpubCreator()

    def testGetBookEpubGetsBook(self):
        """Given a path to a .epub file, when it exists on disk,
        an instance of the book object is created."""
        self.assertIsInstance(self.__getTreasureIsland(), Book)

    def testGetBookEpubGetsCorrectFormatName(self):
        """Given a path to a .epub file, when it exists on disk,
        the returned object has a format of EPUB."""
        b = self.__getTreasureIsland()
        self.assertEquals("EPUB", b.formats[0].Format)

    def testGetBookEpubGetsCorrectLocation(self):
        """Given a path to a .epub file, when it exists on disk,
        the returned object has the given location on disk."""
        b = self.__getTreasureIsland()
        self.assertEquals(self.__epubPath, b.formats[0].Location)

    def testGetInvalidEpub(self):
        """Given a path to a .epub file, when it doesn't exist on disk,
        the returned object is null."""
        b = self.__epc.create("bookformats/tests/data/NotAValidEpub.epub")
        self.assertIsNone(b)

    def __getTreasureIsland(self):
        return self.__epc.create(self.__epubPath)