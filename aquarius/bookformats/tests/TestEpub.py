import unittest
from zipfile import BadZipfile

from aquarius.bookformats.Epub import Epub


class TestEpub(unittest.TestCase):
    """Tests for the Epub class"""
    def setUp(self):
        """Common setup operations"""
        self.__book = Epub("aquarius/bookformats/tests/data/TreasureIsland.epub")
      
    def testLoadingInvalidEpubRaisesBadZipFileException(self):
        """Given a file, when it is an invalid zip file, then raise the
        BadZipFile exception"""
        badEpubPath = "aquarius/bookformats/tests/data/NotAValidEpub.epub"
        self.assertRaises(BadZipfile, Epub, badEpubPath)
        
    def testTitleAttributeIsSetCorrectlyAfterLoading(self):
        """Given a file, when it's a valid epub file, the returned book object
        has the correct Title attribute set"""
        self.assertEqual("Treasure Island", self.__book.title)
        
    def testAuthorAttributeIsSetCorrectlyAfterLoading(self):
        """Given a file, when it's a valid epub file, the returned book object
        has the correct Author attribute set"""
        self.assertEqual("Robert Louis Stevenson", self.__book.author)