import unittest
from unittest.mock import Mock
from aquarius.Persistence import Persistence
from aquarius.objects.Book import Book
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
from aquarius.persistence.sqlitepersistence.SqlitePersistence import SqlitePersistence


class TestSqlitePersistence(unittest.TestCase):

    def setUp(self):
        self.__book_search = Mock(SearchBook)
        self.__book_details = Mock(GetBookDetails)
        self.__add_book = Mock(AddBook)
        self.__add_book_type = Mock(AddBookType)
        self.__get_book_type = Mock(GetBookType)
        self.__list_books_by_first_letter = Mock(ListBooksByFirstLetter)
        self.__get_book_by_title_and_author = Mock(GetBookByTitleAndAuthor)
        self.__add_book_format = Mock(AddBookFormat)
        self.__format_exists = Mock(FormatExists)

        self.__query_factory = Mock(QueryFactory)
        self.__query_factory.create_book_search = Mock(return_value=self.__book_search)
        self.__query_factory.create_get_book_details = Mock(return_value=self.__book_details)
        self.__query_factory.create_add_book = Mock(return_value=self.__add_book)
        self.__query_factory.create_add_book_type = Mock(return_value=self.__add_book_type)
        self.__query_factory.create_get_book_type = Mock(return_value=self.__get_book_type)
        self.__query_factory.create_first_book_by_letter = Mock(return_value=self.__list_books_by_first_letter)
        self.__query_factory.create_get_book_by_title_and_author = Mock(return_value=self.__get_book_by_title_and_author)
        self.__query_factory.create_add_book_format = Mock(return_value=self.__add_book_format)
        self.__query_factory.create_format_exists = Mock(return_value=self.__format_exists)

        self.__target = SqlitePersistence(self.__query_factory)

    def test_search_books_uses_query_factory(self):
        self.__target.search_books("Moo")
        self.__assert_called(self.__query_factory.create_book_search)

    def test_search_books_calls_search_object(self):
        self.__target.search_books("Moo")
        self.__assert_called(self.__book_search.execute)

    def test_get_book_details_uses_query_factory(self):
        self.__target.get_book_details(1)
        self.__assert_called(self.__query_factory.create_get_book_details)

    def test_get_book_details_calls_get_book_details_object(self):
        self.__target.get_book_details(1)
        self.__assert_called(self.__book_details.get_book_details)

    def test_add_book_uses_query_factory(self):
        self.__target.add_book(None)
        self.__assert_called(self.__query_factory.create_add_book)

    def test_add_book_calls_add_book_object(self):
        self.__target.add_book(None)
        self.__assert_called(self.__add_book.add_book)

    def test_add_book_type_uses_query_factory(self):
        self.__target.add_book_type(None)
        self.__assert_called(self.__query_factory.create_add_book_type)

    def test_add_book_type_calls_add_book_type_object(self):
        self.__target.add_book_type(None)
        self.__assert_called(self.__add_book_type.add_book_type)

    def test_book_type_calls_query_factory(self):
        self.__target.get_book_type("EPUB")
        self.__assert_called(self.__query_factory.create_get_book_type)

    def test_get_book_type_calls_get_book_type_object(self):
        self.__target.get_book_type("EPUB")
        self.__assert_called(self.__get_book_type.get_book_type)

    def test_list_books_by_first_letter_uses_query_factory(self):
        self.__target.list_books_by_first_letter("B")
        self.__assert_called(self.__query_factory.create_first_book_by_letter)

    def test_list_books_by_first_letter_calls_the_query_object(self):
        self.__target.list_books_by_first_letter("B")
        self.__assert_called(self.__list_books_by_first_letter.list_books_by_first_letter)

    def test_get_book_by_title_and_author_uses_query_factory(self):
        self.__target.get_book_by_title_and_author(Book())
        self.__assert_called(self.__query_factory.create_get_book_by_title_and_author)

    def test_get_book_by_title_and_author_calls_query_object(self):
        self.__target.get_book_by_title_and_author(Book())
        self.__assert_called(self.__get_book_by_title_and_author.execute)

    def test_add_book_format_uses_query_factory(self):
        self.__target.add_book_format(book_id=0, book_format=None)
        self.__assert_called(self.__query_factory.create_add_book_format)

    def test_add_book_format_calls_command_object(self):
        self.__target.add_book_format(book_id=0, book_format=None)
        self.__assert_called(self.__add_book_format.execute)

    def test_format_exists_uses_query_factory(self):
        self.__target.format_exists(book_id=0, book_format=None)
        self.__assert_called(self.__query_factory.create_format_exists)

    def test_format_exists_calls_command_object(self):
        self.__target.format_exists(book_id=0, book_format=None)
        self.__assert_called(self.__format_exists.execute)

    def __assert_called(self, method):
        self.assertTrue(method.called)

    def test_implements_persistence(self):
        self.assertIsInstance(self.__target, Persistence)