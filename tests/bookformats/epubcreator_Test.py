import unittest

from aquarius.bookformats.epubcreator import EpubCreator


class TestEpubCreator(unittest.TestCase):

    def setUp(self):
        self.__epubPath = "tests/data/TreasureIsland.epub"
        self.__epc = EpubCreator()

    def test_get_epub_gets_correct_format_name(self):
        b = self.__getTreasureIsland()
        self.assertEquals("EPUB", b.formats[0].Format)

    def test_get_epub_gets_correct_location(self):
        b = self.__getTreasureIsland()
        self.assertEquals(self.__epubPath, b.formats[0].Location)

    def test_get_invalid_epub_returns_none(self):
        b = self.__epc.create("tests/data/NotAValidEpub.epub")
        self.assertIsNone(b)

    def __getTreasureIsland(self):
        return self.__epc.create(self.__epubPath)