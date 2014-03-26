import unittest
from unittest.mock import Mock
from aquarius.persistence.sqlitepersistence.Connection import Connection

from aquarius.persistence.sqlitepersistence.ListBooksByFirstLetter import ListBooksByFirstLetter


class TestListBooksByFirstLetter(unittest.TestCase):

    def setUp(self):
        self.__conn = Connection(None)
        self.__l = ListBooksByFirstLetter(self.__conn)

    def test_calling_list_books_by_first_letter_makes_correct_calls(self):
        self.__conn.execute_sql_fetch_all_with_params = \
            Mock(return_value=[])
        self.__l.list_books_by_first_letter("A")
        self.assertEquals(1, self.__conn.execute_sql_fetch_all_with_params.called)

