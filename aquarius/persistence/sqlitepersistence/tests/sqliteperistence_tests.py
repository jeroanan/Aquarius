import unittest
from unittest.mock import Mock
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.AddBookType import AddBookType
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
        self.__setup_list_books_by_first_letter_spy()

    def __setup_add_book_mock(self):
        self.__add_book = AddBook(None)
        self.__add_book.add_book = Mock()
        self.__p.set_add_book(self.__add_book)

    def __setup_get_book_details_mock(self):
        self.__book_details = GetBookDetails(None)
        self.__book_details.get_book_details = Mock()
        self.__p.set_get_book_details(self.__book_details)

    def __setup_book_search_mock(self):
        self.__book_search = SearchBook(None)
        self.__book_search.search_books = Mock()
        self.__p.set_book_search(self.__book_search)

    def __setup_add_book_type_mock(self):
        self.__add_book_type = AddBookType(None)
        self.__add_book_type.add_book_type = Mock()
        self.__p.set_add_book_type(self.__add_book_type)

    def __setup_get_book_type_mock(self):
        self.__get_book_type = GetBookType()
        self.__get_book_type.get_book_type = Mock()
        self.__p.set_get_book_type(self.__get_book_type)

    def __setup_list_books_by_first_letter_spy(self):
        self.__list_books_by_first_letter = ListBooksByFirstLetter()
        self.__list_books_by_first_letter.list_books_by_first_letter = Mock()
        self.__p.set_first_book_by_letter(self.__list_books_by_first_letter)

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
