import unittest
from unittest.mock import Mock
from aquarius.objects.Book import Book
from aquarius.persistence.sqlitepersistence.Connection import Connection
from aquarius.persistence.sqlitepersistence.GetBookByTitleAndAuthor import GetBookByTitleAndAuthor


class TestGetBookByTitleAndAuthor(unittest.TestCase):

    def test_book_exists_returns_book(self):
        conn = Mock(Connection)
        conn.execute_sql_fetch_all_with_params = lambda x, y: [[0, "Title", "Author"]]
        o = GetBookByTitleAndAuthor(conn)

        book = o.execute(Book())
        self.assertEquals(0, book.id)

    def test_book_exists_returns_minus_one(self):
        conn = Mock(Connection)
        conn.execute_sql_fetch_all_with_params = lambda x, y: []
        o = GetBookByTitleAndAuthor(conn)

        book = o.execute(Book())
        self.assertEquals("", book.id)
