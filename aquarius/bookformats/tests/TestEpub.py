import unittest
from zipfile import BadZipfile

from aquarius.bookformats.Epub import Epub


class TestEpub(unittest.TestCase):
    
    def setUp(self):
        self.__book = Epub("aquarius/bookformats/tests/data/TreasureIsland.epub")
      
    def testLoadingInvalidEpubRaisesBadZipFileException(self):
        self.assertRaises(BadZipfile, Epub, "aquarius/bookformats/tests/data/NotAValidEpub.epub")
        
    def testTitleAttributeIsSetCorrectlyAfterLoading(self):
        self.assertEqual("Treasure Island", self.__book.title)
        
    def testAuthorAttributeIsSetCorrectlyAfterLoading(self):
        self.assertEqual("Robert Louis Stevenson", self.__book.author)