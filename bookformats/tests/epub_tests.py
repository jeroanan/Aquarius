from bookformats.epub import epub
import unittest

class epub_tests(unittest.TestCase):
    
    def testLoad(self):
        book = epub("bookformats/tests/data/TreasureIsland.epub").Load()
        
    def testGetsTitle(self):
        book = epub("bookformats/tests/data/TreasureIsland.epub").Load()
        self.assertEqual("Treasure Island", book.Title)
        