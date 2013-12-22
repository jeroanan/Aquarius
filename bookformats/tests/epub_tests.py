from bookformats.epub import epub
import unittest
from zipfile import BadZipfile

class epub_tests(unittest.TestCase):
    
    def setUp(self):
        self.__book = epub("bookformats/tests/data/TreasureIsland.epub").Load()
        
    def testLoadingEpubGetsTitle(self):
        self.assertEqual("Treasure Island", self.__book.Title)
        
    def testLoadingEpubGetsAuthor(self):
        self.assertEqual("Robert Louis Stevenson", self.__book.Author)       
            
    def testLoadingInvalidEpubRaisesBadZipFileException(self):
        self.assertRaises(BadZipfile, epub, "bookformats/tests/data/NotAValidEpub.epub")
        
    def testLoadingEpubGetsValidFormatFormatCode(self):
        self.assertEqual("EPUB", self.__book.Formats[0].Format)
        
    def testLoadingEpubGetsValidFormatLocation(self):
        self.assertTrue(self.__book.Formats[0].Location.startswith("bookformats/tests/data/TreasureIsland.epub"))