import unittest

from aquarius.aquarius import aquarius as app
from aquarius.objects.book import book


class aquarius_tests(unittest.TestCase):
    
    def setUp(self):
        self.__app = app("persistor", "dummy", "whatever")
        self.__gotCallback = False
        
    def testSearchBooks(self):
        self.__app.SearchBooks("")
        
    def testListBooksByFirstLetter(self):
        self.__app.ListBooksByFirstLetter("b")
        
    def testGetBookDetails(self):        
        self.__app.GetBookDetails(0)
                        
    def testGetBookType(self):
        self.__app.GetBookType("EPUB")
        
    def testHarvestBooks(self):
        self.__app.HarvestBooks()

    def testAddBook(self):
        b = book()
        b.Author = "J. R. Hartley"
        b.Title = "Fly Fishing"
        self.__app.AddBook(b)
        
    def testCallMain(self):
        self.__app.Main()
