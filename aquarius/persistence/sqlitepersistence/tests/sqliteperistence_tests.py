import os
import unittest
from unittest.mock import Mock

from Config import Config
from aquarius.objects.booktype import booktype
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook
from aquarius.persistence.sqlitepersistence.SqlitePersistence import Persistence
from aquarius.objects.Book import Book


class TestSqlitePersistence(unittest.TestCase):

    def setUp(self):        
        self.__setupConfigMock()
        self.__addbook = AddBook()
        self.__setupSearchBookMock()
        self.__p = Persistence(self.__config, self.__searchbook, self.__addbook)
    
    def __setupConfigMock(self):
        self.__config = Config()
        self.__config.sqllite_database_path = "./database.db"

    def __setupSearchBookMock(self):
        self.__searchbook = SearchBook()
        self.__searchbook.search_books = Mock(return_value=None)
        self.__searchbook.get_book_details = Mock(return_value=None)
        
    def tearDown(self):
        os.remove(self.__config.sqllite_database_path)
            
    def testSearchingBooksCausesTheSearchMethodToBeCalled(self):
        self.__p.search_books("Moo")
        self.assertTrue(self.__searchbook.search_books.called)
    
    def testCallingGetBookDetailsCausesTheGetBookDetailsMethodToBeCalled(self):
        self.__p.get_book_details(1)
        self.assertTrue(self.__searchbook.get_book_details.called)
    
    def testCallingAddBookCausesTheAddBookMethodToBeCalled(self):
        self.__addbook.add_book = Mock(return_value=None)
        self.__p.add_book(None)
        self.assertTrue(self.__addbook.add_book.called)

    def testGetBookTypeGetsRightBookFormatName(self):
        self.__p.add_book_type(self.__getSomeFormatBookType())
        self.assertEqual("SomeFormat", self.__p.get_book_type("SomeFormat").Format)
        
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

    def testListBooksByFirstLetterGetsEmptySetWhenNotFound(self):
        self.assertEquals(0, len(list(self.__p.list_books_by_first_letter("t"))))
        
    def testListBooksGetsOneWhenABookIsFound(self):
        self.__p.add_book(self.__getTreasureIsland())
        r = self.__p.list_books_by_first_letter("t")
        self.assertEquals(1, len(list(r)))
