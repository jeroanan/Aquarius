import unittest
from unittest.mock import Mock
from aquarius.persistence.sqlitepersistence.Connection import Connection
from aquarius.persistence.sqlitepersistence.FormatExists import FormatExists


class TestFormatExists(unittest.TestCase):

    def test_instantiation(self):
        FormatExists(Mock(Connection))

    def test_book_does_not_exist_return_false(self):
        conn = self.setup_mock([])
        a = FormatExists(conn)
        self.assertFalse(a.execute(book_id=1, book_format="epub"))

    def test_book_exists_returns_true(self):
        conn = self.setup_mock([1])
        a = FormatExists(conn)
        self.assertTrue(a.execute(book_id=1, book_format="epub"))

    def setup_mock(self, return_value):
        conn = Mock(Connection)
        conn.execute_sql_fetch_all_with_params = Mock(return_value=return_value)
        return conn