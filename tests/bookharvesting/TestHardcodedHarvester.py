from aquarius.Aquarius import Aquarius
from aquarius.bookharvesting.HardcodedHarvester import HardcodedHarvester
from Config import Config
import unittest


class TestHardcodedHarvester(unittest.TestCase):

    def setUp(self):
        self.__a = self.App()
        self.__c = Config()
        
    def test_DoHarvest(self):
        h = HardcodedHarvester(self.__a, self.__c)
        h.do_harvest()
        self.__check_book()
        self.__check_format()
        
    def __check_book(self):
        self.assertEqual(1, len(self.__a.books))
        self.assertEqual("J. R. Hartley", self.__a.books[0].author)
        self.assertEqual("Fly Fishing", self.__a.books[0].title)
    
    def __check_format(self):
        self.assertEqual(1, len(self.__a.books[0].formats))
        self.assertEqual("EPUB", self.__a.books[0].formats[0].Format)
        self.assertEqual("/tmp/test.epub", self.__a.books[0].formats[0].Location)
                
    class App(Aquarius):
        
        def __init__(self):
            self.books = []
        
        def add_book(self, book):
            self.books.append(book)
