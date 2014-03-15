import unittest

from aquarius.objects.BookType import BookType
from aquarius.persistence.sqlitepersistence.AddBookType import AddBookType
from aquarius.persistence.sqlitepersistence.tests.Mocks.ConnectionSpy import ConnectionSpy


class TestAddBookType(unittest.TestCase):

    def setUp(self):
        self.__a = AddBookType()
        self.__connection = ConnectionSpy()

    def testAddBookTypeCallsCorrectCollaboratingObjects(self):
        bt = BookType()
        bt.Format = "EPUB"
        bt.MimeType = "MIME"
        self.__a.add_book_type(bt, self.__connection)
        self.assertEquals(1, self.__connection.fetch_none_with_params_calls)