from aquarius import aquarius
from bookharvesting.hardcodedharvester import hardcodedharvester

import unittest

class hardcodedharvester_tests(unittest.TestCase):
    
    def setUp(self):
        self.__a = self.__app()    

    def test_DoHarvest(self):
        h = hardcodedharvester(self.__a)
        h.doHarvest()      
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
                
    class __app(aquarius):
        
        def __init__(self):
            self.books = []
        
        def AddBook(self, book):
            self.books.append(book)
            