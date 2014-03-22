import unittest

from aquarius.bookformats.epubcreator import EpubCreator
from aquarius.objects.Book import Book


class TestEpubCreator(unittest.TestCase):

    def setUp(self):
        self.__epubPath = "aquarius/bookformats/tests/data/TreasureIsland.epub"
        self.__epc = EpubCreator()

    def testGetBookEpubGetsBook(self):
        self.assertIsInstance(self.__getTreasureIsland(), Book)

    def testGetBookEpubGetsCorrectFormatName(self):
        b = self.__getTreasureIsland()
        self.assertEquals("EPUB", b.formats[0].Format)

    def testGetBookEpubGetsCorrectLocation(self):
        b = self.__getTreasureIsland()
        self.assertEquals(self.__epubPath, b.formats[0].Location)

    def testGetInvalidEpub(self):
        b = self.__epc.create("bookformats/tests/data/NotAValidEpub.epub")
        self.assertIsNone(b)

    def __getTreasureIsland(self):
        return self.__epc.create(self.__epubPath)