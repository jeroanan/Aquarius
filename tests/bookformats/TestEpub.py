import unittest
from zipfile import BadZipfile

from aquarius.bookformats.Epub import Epub


class TestEpub(unittest.TestCase):

    def setUp(self):
        path = "tests/data/TreasureIsland.epub"
        self.__book = Epub(path)
      
    def test_load_raises_badzipfile_when_invalid_file(self):
        bad_epub_path = "tests/data/NotAValidEpub.epub"
        self.assertRaises(BadZipfile, Epub, bad_epub_path)
        
    def test_load_sets_tittle(self):
        self.assertEqual("Treasure Island", self.__book.title)
        
    def test_load_sets_author(self):
        self.assertEqual("Robert Louis Stevenson", self.__book.author)

    def test_load_sets_rights(self):
        self.assertEqual("Public domain in the USA.", self.__book.rights)

    def test_load_sets_identifier(self):
        self.assertEqual("http://www.gutenberg.org/ebooks/120", self.__book.identifier)

    def test_load_sets_language(self):
        self.assertEqual("en", self.__book.language)