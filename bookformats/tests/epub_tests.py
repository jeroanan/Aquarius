from bookformats.epub import epub
import unittest

class epub_tests(unittest.TestCase):
    
    def setUp(self):
        self.__book = epub("bookformats/tests/data/TreasureIsland.epub").Load()
        
    def testGetsTitle(self):
        self.assertEqual("Treasure Island", self.__book.Title)
        
    def testGetsAuthor(self):
        self.assertEqual("Robert Louis Stevenson", self.__book.Author)       
            