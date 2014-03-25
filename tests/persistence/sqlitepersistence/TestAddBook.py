import unittest

from aquarius.objects.Book import Book
from aquarius.objects.BookFormat import BookFormat
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from tests.persistence.sqlitepersistence.Mocks.ConnectionSpy import ConnectionSpy


class TestAddBook(unittest.TestCase):

    def setUp(self):
        self.__conn = ConnectionSpy()
        self.__add_book = AddBook(self.__conn)

    def test_adding_book_with_one_format_causes_the_correct_database_calls(self):
        self.__add_book.add_book(self.__get_treasure_island_with_format("EPUB"))
        self.assertEquals(2, self.__conn.fetch_all_with_params_calls)
        self.assertEqual(2, self.__conn.fetch_none_with_params_calls)
        self.assertEquals(1, self.__conn.get_last_row_id_calls)

    def test_adding_two_identical_books_causes_only_one_to_be_written(self):
        b = self.__get_treasure_island()
        self.__add_book.add_book(b)
        self.assertEquals(1, self.__conn.fetch_all_with_params_calls)
        self.assertEqual(1, self.__conn.fetch_none_with_params_calls)
        self.assertEquals(1, self.__conn.get_last_row_id_calls)

    def __get_treasure_island_with_format(self, format_code):
        b = self.__get_treasure_island()
        bf = BookFormat()
        bf.Format = format_code
        b.formats.append(bf)
        return b

    def __get_treasure_island(self):
        b = Book()
        b.id = "1"
        b.title = "Treasure Island"
        b.author = "Robert Louis Stevenson"
        return b

