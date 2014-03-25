import unittest
from unittest.mock import Mock
from aquarius.objects.Book import Book
from aquarius.persistence.sqlitepersistence.Connection import Connection
from aquarius.persistence.sqlitepersistence.GetExistingBookId import GetExistingBookId


class TestGetExistingBookId(unittest.TestCase):

    def test_book_exists_returns_book(self):
        conn = Mock(Connection)
        conn.execute_sql_fetch_all_with_params = lambda x, y: [[0]]
        o = GetExistingBookId(conn)

        book_id = o.get_existing_book_id(Book())
        self.assertEquals(0, book_id)

    def test_book_exists_returns_minus_one(self):
        conn = Mock(Connection)
        conn.execute_sql_fetch_all_with_params = lambda x, y: []
        o = GetExistingBookId(conn)

        book_id = o.get_existing_book_id(Book())
        self.assertEquals(-1, book_id)
