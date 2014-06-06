import unittest
from unittest.mock import _get_target
from aquarius.Persistence import Persistence


class TestPersistence(unittest.TestCase):

    def setUp(self):
        self.__target = Persistence()

    def test_search_books(self):
        self.__assert_not_implemented(self.__target.search_books, "search_term")

    def test_get_book_details(self):
        self.__assert_not_implemented(self.__target.get_book_details, "book_id")

    def test_add_book(self):
        self.__assert_not_implemented(self.__target.add_book, "book")

    def test_add_book_type(self):
        self.__assert_not_implemented(self.__target.add_book_type, "book_type")

    def test_get_book_type(self):
        self.__assert_not_implemented(self.__target.get_book_type, "book_type")

    def test_list_books_by_first_letter(self):
        self.__assert_not_implemented(self.__target.list_books_by_first_letter, "first_letter")

    def test_get_book_by_title_and_author(self):
        self.__assert_not_implemented(self.__target.get_book_by_title_and_author, "book")

    def test_add_book_format(self):
        self.assertRaises(NotImplementedError, self.__target.add_book_format, "book_id", "book_format")

    def test_format_exists(self):
        self.assertRaises(NotImplementedError, self.__target.format_exists, "book_id", "book_format")

    def __assert_not_implemented(self, method, arg):
        with self.assertRaises(NotImplementedError):
            method(arg)
