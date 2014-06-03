import unittest
from unittest.mock import Mock
from aquarius.objects.Book import Book
from aquarius.objects.BookFormat import BookFormat
from aquarius.persistence.sqlitepersistence.AddBookFormat import AddBookFormat
from aquarius.persistence.sqlitepersistence.Connection import Connection


class TestAddBookFormats(unittest.TestCase):

    def test_instantiation(self):
        AddBookFormat(Mock(Connection))

    def test_execute_calls_database(self):
        connection = Mock(Connection)
        a = AddBookFormat(connection)
        book = self.__get_treasure_island()
        book_format = self.__get_format()

        a.execute(book.id, book_format)

        self.assertTrue(connection.execute_sql_with_params.called)

    def __get_treasure_island(self):
        b = Book()
        b.id = "1"
        b.title = "Treasure Island"
        b.author = "Robert Louis Stevenson"
        return b

    def __get_format(self):
        bf = BookFormat()
        bf.Format = "epub"
        bf.Location = "/dev/null"
        return bf