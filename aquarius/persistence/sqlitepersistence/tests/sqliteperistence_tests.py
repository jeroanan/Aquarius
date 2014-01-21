
import os
import unittest
from unittest.mock import Mock

from aquarius.objects.booktype import booktype
from aquarius.objects.Book import Book
from aquarius.persistence.sqlitepersistence.tests.Mocks.AddBookSpy import AddBookSpy
from aquarius.persistence.sqlitepersistence.tests.Mocks.GetBookDetailsSpy \
    import GetBookDetailsSpy
from aquarius.persistence.sqlitepersistence.tests.Mocks.SearchBookSpy \
    import SearchBookSpy
from aquarius.persistence.sqlitepersistence.SqlitePersistence \
    import SqlitePersistence


class TestSqlitePersistence(unittest.TestCase):

    def setUp(self):
        self.__p = SqlitePersistence()
        self.__setupSpies()

    def __setupSpies(self):
        self.__setupAddBookSpy()
        self.__setupGetBookDetailsSpy()
        self.__setupBookSearchSpy()

    def __setupAddBookSpy(self):
        self.__addbook = AddBookSpy()
        self.__p.set_add_book(self.__addbook)

    def __setupGetBookDetailsSpy(self):
        self.__book_details = GetBookDetailsSpy()
        self.__p.set_get_book_details(self.__book_details)

    def __setupBookSearchSpy(self):
        self.__book_search = SearchBookSpy()
        self.__p.set_book_search(self.__book_search)

    def tearDown(self):
        pass#os.remove(self.__config.sqllite_database_path)

    def testSearchingBooksCausesTheSearchMethodToBeCalled(self):
        self.__p.search_books("Moo")
        self.assertEqual(1, self.__book_search.search_books_calls)

    def testCallingGetBookDetailsCausesTheGetBookDetailsMethodToBeCalled(self):
        self.__p.get_book_details(1)
        self.assertEquals(1, self.__book_details.get_book_details_calls)

    def testCallingAddBookCausesTheAddBookMethodToBeCalled(self):
        self.__p.add_book(None)
        self.assertEquals(1, self.__addbook.add_book_calls)

    @unittest.skip
    def testGetBookTypeGetsRightBookFormatName(self):
        self.__p.add_book_type(self.__getSomeFormatBookType())
        self.assertEqual("SomeFormat", self.__p.get_book_type("SomeFormat").Format)

    @unittest.skip
    def testGetBookTypeGetsRightMimeType(self):
        self.__p.add_book_type(self.__getSomeFormatBookType())
        bt = self.__p.get_book_type("SomeFormat")
        self.assertEqual("text/someformat", bt.MimeType)

    @staticmethod
    def __getSomeFormatBookType():
        bt = booktype()
        bt.Format = "SomeFormat"
        bt.MimeType = "text/someformat"
        return bt
    
    @staticmethod
    def __getTreasureIsland():
        b = Book()
        b.author = "Robert Louis Stephenson"
        b.title = "Treasure Island"
        return b
    
    def testGetBookTypesReturnsNoneWhenBookTypeNotFound(self):
        self.assertIsNone(self.__p.get_book_type("DoesntExist"))
        
    def testListBooksByFirstLetter(self):
        self.__p.list_books_by_first_letter("t")

    @unittest.skip
    def testListBooksByFirstLetterGetsEmptySetWhenNotFound(self):
        self.assertEquals(0, len(list(self.__p.list_books_by_first_letter("t"))))
        
    def testListBooksGetsOneWhenABookIsFound(self):
        self.__p.add_book(self.__getTreasureIsland())
        r = self.__p.list_books_by_first_letter("t")
        self.assertEquals(1, len(list(r)))
