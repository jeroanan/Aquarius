import unittest

from aquarius.persistence.sqlitepersistence.ListBooksByFirstLetter \
    import ListBooksByFirstLetter
from aquarius.persistence.sqlitepersistence.tests.Mocks.ConnectionSpy \
    import ConnectionSpy
from aquarius.persistence.sqlitepersistence.tests.Mocks.ParameterSanitiserSpy \
    import ParameterSanitiserSpy


class TestListBooksByFirstLetter(unittest.TestCase):

    def setUp(self):
        self.__sanitiser = ParameterSanitiserSpy()
        self.__conn = ConnectionSpy()
        self.__l = ListBooksByFirstLetter()
        self.__l.set_parameter_sanitiser(self.__sanitiser)

    def testCanSetParameterSanitiser(self):
        self.__l.set_parameter_sanitiser(None)

    def testCallingListBooksByFirstLetterMakesCorrectCalls(self):
        self.__l.list_books_by_first_letter("A", self.__conn)
        self.assertEquals(1, self.__sanitiser.sanitise_calls)
        self.assertEquals(1, self.__conn.fetch_all_calls)