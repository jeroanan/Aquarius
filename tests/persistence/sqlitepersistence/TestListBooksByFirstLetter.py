import unittest

from aquarius.persistence.sqlitepersistence.ListBooksByFirstLetter import ListBooksByFirstLetter
from tests.persistence.sqlitepersistence.Mocks.ConnectionSpy import ConnectionSpy


class TestListBooksByFirstLetter(unittest.TestCase):

    def setUp(self):
        self.__conn = ConnectionSpy()
        self.__l = ListBooksByFirstLetter(self.__conn)

    def test_calling_list_books_by_first_letter_makes_correct_calls(self):
        self.__l.list_books_by_first_letter("A")
        self.assertEquals(1, self.__conn.fetch_all_with_params_calls)