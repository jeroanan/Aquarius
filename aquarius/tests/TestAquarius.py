import unittest
from unittest.mock import Mock

from aquarius.Aquarius import Aquarius
from aquarius.bookharvesting.HardcodedHarvester import HardcodedHarvester
from aquarius.objects.Book import Book


class TestAquarius(unittest.TestCase):
    
    def setUp(self):
        self.__app = Aquarius("persistor", "dummy", "whatever")
        self.__gotCallback = False

    def testSearchBooks(self):
        self.__app.search_books("")
        
    def testListBooksByFirstLetter(self):
        self.__app.list_books_by_first_letter("b")
        
    def testGetBookDetails(self):        
        self.__app.get_book_details(0)
                        
    def testGetBookType(self):
        self.__app.get_book_type("EPUB")

    def testAddBook(self):
        b = Book()
        b.author = "J. R. Hartley"
        b.title = "Fly Fishing"
        self.__app.add_book(b)
        
    def testCallMain(self):
        self.__app.main()

    def testCanSetPersistor(self):
        self.__app.set_persistor(None)

    def setup_harvester_mock(self):
        a = Aquarius("hardcoded", None, None)
        harvester = HardcodedHarvester(a, None)
        harvester.do_harvest = Mock()
        a.set_harvester(harvester)
        return a, harvester

    def test_calling_harvest_books_calls_harvester(self):
        a, harvester = self.setup_harvester_mock()
        a.harvest_books()
        self.assertTrue(harvester.do_harvest.called)

    def test_calling_harvest_books_does_not_call_harvester_when_is_harvesting_set(self):
        a, harvester = self.setup_harvester_mock()
        a.is_harvesting = True
        a.harvest_books()
        self.assertFalse(harvester.do_harvest.called)