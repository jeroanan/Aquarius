from bookformats.epub import epub
import unittest
from zipfile import BadZipfile

class epub_tests(unittest.TestCase):
    
    def setUp(self):
        self.__book = epub("bookformats/tests/data/TreasureIsland.epub")
      
    def testLoadingInvalidEpubRaisesBadZipFileException(self):
        self.assertRaises(BadZipfile, epub, "bookformats/tests/data/NotAValidEpub.epub")
        
    def testTitleAttributeIsSetCorrectlyAfterLoading(self):
        self.assertEqual("Treasure Island", self.__book.Title)
        
    def testAuthorAttributeIsSetCorrectlyAfterLoading(self):
        self.assertEqual("Robert Louis Stevenson", self.__book.Author)