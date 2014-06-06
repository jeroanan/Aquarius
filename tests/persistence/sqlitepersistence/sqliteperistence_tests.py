import unittest
from unittest.mock import Mock
from aquarius.Persistence import Persistence
from aquarius.objects.Book import Book
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.AddBookFormat import AddBookFormat
from aquarius.persistence.sqlitepersistence.AddBookType import AddBookType
from aquarius.persistence.sqlitepersistence.Connection import Connection
from aquarius.persistence.sqlitepersistence.FormatExists import FormatExists
from aquarius.persistence.sqlitepersistence.GetBookByTitleAndAuthor import GetBookByTitleAndAuthor
from aquarius.persistence.sqlitepersistence.GetBookDetails import GetBookDetails
from aquarius.persistence.sqlitepersistence.GetBookType import GetBookType
from aquarius.persistence.sqlitepersistence.ListBooksByFirstLetter import ListBooksByFirstLetter
from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook
from aquarius.persistence.sqlitepersistence.SqlitePersistence import SqlitePersistence


class TestSqlitePersistence(unittest.TestCase):

    def setUp(self):
        self.__p = SqlitePersistence()
        self.__setup_mocks()

    def __setup_mocks(self):
        self.__setup_add_book_mock()
        self.__setup_get_book_details_mock()
        self.__setup_book_search_mock()
        self.__setup_add_book_type_mock()
        self.__setup_get_book_type_mock()
        self.__setup_list_books_by_first_letter_mock()
        self.__setup_add_book_format_mock()
        self.__setup_format_exists()

    def __setup_add_book_mock(self):
        self.__add_book = AddBook(Mock(Connection))
        self.__add_book.add_book = Mock()
        self.__p.get_add_book = lambda x: self.__add_book

    def __setup_get_book_details_mock(self):
        self.__book_details = GetBookDetails(Mock(Connection))
        self.__book_details.get_book_details = Mock()
        self.__p.get_get_book_details = lambda x: self.__book_details

    def __setup_book_search_mock(self):
        self.__book_search = SearchBook(Mock(Connection))
        self.__book_search.search_books = Mock()
        self.__p.get_book_search = lambda x: self.__book_search

    def __setup_add_book_type_mock(self):
        self.__add_book_type = AddBookType(Mock(Connection))
        self.__add_book_type.add_book_type = Mock()
        self.__p.get_add_book_type = lambda x: self.__add_book_type

    def __setup_get_book_type_mock(self):
        self.__get_book_type = GetBookType(Mock(Connection))
        self.__get_book_type.get_book_type = Mock()
        self.__p.get_get_book_type = lambda x: self.__get_book_type

    def __setup_list_books_by_first_letter_mock(self):
        self.__list_books_by_first_letter = ListBooksByFirstLetter(Mock(Connection))
        self.__list_books_by_first_letter.list_books_by_first_letter = Mock()
        self.__p.get_first_book_by_letter = lambda x: self.__list_books_by_first_letter

    def __setup_add_book_format_mock(self):
        self.__add_book_format = AddBookFormat(Mock(Connection))
        self.__add_book_format.execute = Mock()
        self.__p.get_add_book_format = lambda x: self.__add_book_format

    def __setup_format_exists(self):
        self.__format_exists = FormatExists(Mock(Connection))
        self.__format_exists.execute = Mock()
        self.__p.get_format_exists = lambda x: self.__format_exists

    def test_searching_books_causes_the_search_method_to_be_called(self):
        self.__p.search_books("Moo")
        self.assertTrue(self.__book_search.search_books.called)

    def test_calling_get_book_details_causes_the_get_book_details_method_to_be_called(self):
        self.__p.get_book_details(1)
        self.assertTrue(self.__book_details.get_book_details.called)

    def test_calling_add_book_causes_the_add_book_method_to_be_called(self):
        self.__p.add_book(None)
        self.assertTrue(self.__add_book.add_book.called)

    def test_calling_add_book_type_causes_the_add_book_type_method_to_be_called(self):
        self.__p.add_book_type(None)
        self.assertTrue(self.__add_book_type.add_book_type.called)

    def test_calling_get_book_type_causes_the_get_book_type_method_to_be_called(self):
        self.__p.get_book_type("EPUB")
        self.assertTrue(self.__get_book_type.get_book_type.called)

    def test_calling_list_first_book_by_letter_causes_the_correct_method_to_be_called(self):
        self.__p.list_books_by_first_letter("B")
        self.assertTrue(self.__list_books_by_first_letter.list_books_by_first_letter.called)

    def test_get_book_by_title_and_author(self):
        get_book_by_title_and_author = Mock(GetBookByTitleAndAuthor)
        self.__p.get_get_book_by_title_and_author = lambda x: get_book_by_title_and_author
        self.__p.get_book_by_title_and_author(Book())
        self.assertTrue(get_book_by_title_and_author.execute.called)

    def test_add_book_format_calls_command_object(self):
        self.__p.add_book_format(book_id=0, book_format=None)
        self.assertTrue(self.__add_book_format.execute.called)

    def test_format_exists_calls_command_object(self):
        self.__p.format_exists(book_id=0, book_format=None)
        self.assertTrue(self.__format_exists.execute.called)

    def test_implements_persistence(self):
        self.assertIsInstance(self.__p, Persistence)