import unittest

from aquarius.persistence.sqlitepersistence.ListBooksByFirstLetter import ListBooksByFirstLetter
from aquarius.persistence.sqlitepersistence.tests.Mocks.ConnectionSpy import ConnectionSpy


class TestListBooksByFirstLetter(unittest.TestCase):

    def setUp(self):
        self.__conn = ConnectionSpy()
        self.__l = ListBooksByFirstLetter()

    def testCallingListBooksByFirstLetterMakesCorrectCalls(self):
        self.__l.list_books_by_first_letter("A", self.__conn)
        self.assertEquals(1, self.__conn.fetch_all_with_params_calls)