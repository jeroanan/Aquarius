import unittest

from aquarius.objects.BookType import BookType
from aquarius.persistence.sqlitepersistence.AddBookType import AddBookType
from aquarius.persistence.sqlitepersistence.tests.Mocks.ConnectionSpy \
    import ConnectionSpy
from aquarius.persistence.sqlitepersistence.tests.Mocks.ParameterSanitiserSpy \
    import ParameterSanitiserSpy


class TestAddBookType(unittest.TestCase):

    def setUp(self):
        self.__a = AddBookType()
        self.__connection = ConnectionSpy()
        self.__parameter_sanitiser = ParameterSanitiserSpy()
        self.__a.set_parameter_sanitiser(self.__parameter_sanitiser)

    def testCanSetParameterSanitiser(self):
        self.__a.set_parameter_sanitiser(None)

    def testAddBookTypeCallsCorrectCollaboratingObjects(self):
        bt = BookType()
        bt.Format = "EPUB"
        bt.MimeType = "MIME"
        self.__a.add_book_type(bt, self.__connection)
        self.assertEquals(1, self.__connection.fetch_none_calls)
        self.assertEquals(1, self.__parameter_sanitiser.sanitise_calls)