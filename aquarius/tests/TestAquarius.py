import unittest

from aquarius.Aquarius import Aquarius
from aquarius.objects.Book import Book


class TestAquarius(unittest.TestCase):
    
    def setUp(self):
        self.__app = Aquarius("persistor", "dummy", "whatever")
        self.__gotCallback = False

    #TODO: These tests don't actually assert anything.
    def testSearchBooks(self):
        self.__app.search_books("")
        
    def testListBooksByFirstLetter(self):
        self.__app.list_books_by_first_letter("b")
        
    def testGetBookDetails(self):        
        self.__app.get_book_details(0)
                        
    def testGetBookType(self):
        self.__app.get_book_type("EPUB")
        
    def testHarvestBooks(self):
        self.__app.harvest_books()

    def testAddBook(self):
        b = Book()
        b.author = "J. R. Hartley"
        b.title = "Fly Fishing"
        self.__app.add_book(b)
        
    def testCallMain(self):
        self.__app.main()

    def testCanSetPersistor(self):
        self.__app.set_persistor(None)