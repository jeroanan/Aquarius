from unittest.mock import Mock
from aquarius.objects.Book import Book
from aquarius.persistence.sqlitepersistence.Connection import Connection
from aquarius.persistence.sqlitepersistence.GetFormatsForBook import GetFormatsForBook

import unittest


class TestGetFormatsForBook(unittest.TestCase):

    def test_execute(self):
        connection = Mock(Connection)
        o = GetFormatsForBook(connection)
        o.execute(Book())
        self.assertTrue(connection.execute_sql_fetch_all_with_params.called)