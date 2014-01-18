from aquarius.Aquarius import Aquarius
from aquarius.bookharvesting.HardcodedHarvester import HardcodedHarvester
from Config import Config
import unittest


class TestHardcodedHarvester(unittest.TestCase):
    """Tests for the hardcoded harvester"""
    def setUp(self):
        """Common setup operations"""
        self.__a = self.App()
        self.__c = Config()
        
    def test_DoHarvest(self):
        """Given a harvest request, then the correct book is harvested"""
        h = HardcodedHarvester(self.__a, self.__c)
        h.do_harvest()
        self.__CheckBook()
        self.__CheckFormat()
        
    def __CheckBook(self):
        self.assertEqual(1, len(self.__a.books))
        self.assertEqual("J. R. Hartley", self.__a.books[0].Author)
        self.assertEqual("Fly Fishing", self.__a.books[0].Title)
    
    def __CheckFormat(self):
        self.assertEqual(1, len(self.__a.books[0].Formats))
        self.assertEqual("EPUB", self.__a.books[0].Formats[0].Format)
        self.assertEqual("/tmp/test.epub", self.__a.books[0].Formats[0].Location)
                
    class App(Aquarius):
        
        def __init__(self):
            self.books = []
        
        def add_book(self, book):
            self.books.append(book)
