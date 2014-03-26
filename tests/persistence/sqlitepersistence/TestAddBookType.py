import unittest

from aquarius.objects.BookType import BookType
from aquarius.persistence.sqlitepersistence.AddBookType import AddBookType
from tests.persistence.sqlitepersistence.Mocks.ConnectionSpy import ConnectionSpy


class TestAddBookType(unittest.TestCase):

    def setUp(self):
        self.__connection = ConnectionSpy()
        self.__a = AddBookType(self.__connection)

    def test_add_book_type_calls_correct_collaborating_objects(self):
        bt = BookType()
        bt.Format = "EPUB"
        bt.MimeType = "MIME"
        self.__a.add_book_type(bt)
        self.assertEquals(1, self.__connection.fetch_none_with_params_calls)