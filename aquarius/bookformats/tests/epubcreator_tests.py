import unittest

from aquarius.bookformats.epubcreator import EpubCreator
from aquarius.objects.book import book


class EpubCreator_tests(unittest.TestCase):

    def setUp(self):
        self.__epubPath = "aquarius/bookformats/tests/data/TreasureIsland.epub"
        self.__epc = EpubCreator()

    def testGetBookEpubGetsBook(self):
        self.assertIsInstance(self.__getTreasureIsland(), book)

    def testGetBookEpubGetsCorrectFormatName(self):
        b = self.__getTreasureIsland()
        self.assertEquals("EPUB", b.Formats[0].Format)

    def testGetBookEpubGetsCorrectLocation(self):
        b = self.__getTreasureIsland()
        self.assertEquals(self.__epubPath, b.Formats[0].Location)

    def testGetInvalidEpub(self):
        b = self.__epc.create("bookformats/tests/data/NotAValidEpub.epub")
        self.assertIsNone(b)

    def __getTreasureIsland(self):
        return self.__epc.create(self.__epubPath)