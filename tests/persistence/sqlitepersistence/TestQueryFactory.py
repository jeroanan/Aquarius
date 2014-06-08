import unittest
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.AddBookFormat import AddBookFormat
from aquarius.persistence.sqlitepersistence.AddBookType import AddBookType
from aquarius.persistence.sqlitepersistence.FormatExists import FormatExists
from aquarius.persistence.sqlitepersistence.GetBookByTitleAndAuthor import GetBookByTitleAndAuthor
from aquarius.persistence.sqlitepersistence.GetBookDetails import GetBookDetails
from aquarius.persistence.sqlitepersistence.GetBookType import GetBookType
from aquarius.persistence.sqlitepersistence.ListBooksByFirstLetter import ListBooksByFirstLetter
from aquarius.persistence.sqlitepersistence.QueryFactory import QueryFactory
from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook


class TestQueryFactory(unittest.TestCase):

    def setUp(self):
        self.__target = QueryFactory()

    def test_create_add_book(self):
        q = self.__target.create_add_book(None)
        self.assertIsInstance(q, AddBook)

    def test_create_get_book_details(self):
        q = self.__target.create_get_book_details(None)
        self.assertIsInstance(q, GetBookDetails)
        
    def test_create_book_search(self):
        q = self.__target.create_book_search(None)
        self.assertIsInstance(q, SearchBook)

    def test_create_add_book_type(self):
        q = self.__target.create_add_book_type(None)
        self.assertIsInstance(q, AddBookType)

    def test_create_get_book_type(self):
        q = self.__target.create_get_book_type(None)
        self.assertIsInstance(q, GetBookType)

    def test_create_first_book_by_letter(self):
        q = self.__target.create_first_book_by_letter(None)
        self.assertIsInstance(q, ListBooksByFirstLetter)
        
    def test_create_get_book_by_title_and_author(self):
        q = self.__target.create_get_book_by_title_and_author(None)
        self.assertIsInstance(q, GetBookByTitleAndAuthor)

    def test_create_add_book_format(self):
        q = self.__target.create_add_book_format(None)
        self.assertIsInstance(q, AddBookFormat)

    def test_create_format_exists(self):
        q = self.__target.create_format_exists(None)
        self.assertIsInstance(q, FormatExists)