import unittest
from unittest.mock import Mock

from aquarius.objects.Book import Book
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.Connection import Connection


class TestAddBook(unittest.TestCase):

    def setUp(self):
        self.__conn = Mock(Connection)
        self.__add_book = AddBook(self.__conn)

    def test_adding_book_causes_the_correct_database_calls(self):
        self.__add_book.add_book(self.__get_treasure_island())
        self.assertTrue(self.__conn.execute_sql_with_params.called)

    def __get_treasure_island(self):
        b = Book()
        b.id = "1"
        b.title = "Treasure Island"
        b.author = "Robert Louis Stevenson"
        return b

