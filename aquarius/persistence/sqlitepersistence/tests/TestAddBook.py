import unittest

from aquarius.objects.Book import Book
from aquarius.objects.BookFormat import BookFormat
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.tests.Mocks.ConnectionSpy \
    import ConnectionSpy
from aquarius.persistence.sqlitepersistence.tests.Mocks.ParameterSanitiserSpy import ParameterSanitiserSpy


class TestAddBook(unittest.TestCase):

    def setUp(self):
        self.__add_book = AddBook()
        self.__conn = ConnectionSpy()

    def testAddingBookWithOneFormatCausesTheCorrectDatabaseCalls(self):
        self.__add_book.add_book(self.__GetTreasureIslandWithFormat("EPUB"),
                                 self.__conn)
        self.assertEquals(2, self.__conn.fetch_all_with_params_calls)
        self.assertEqual(2, self.__conn.fetch_none_with_params_calls)
        self.assertEquals(1, self.__conn.get_last_row_id_calls)

    def testAddingTwoIdenticalBooksCausesOnlyOneToBeWritten(self):
        b = self.__GetTreasureIsland()
        self.__add_book.add_book(b, self.__conn)
        self.assertEquals(1, self.__conn.fetch_all_with_params_calls)
        self.assertEqual(1, self.__conn.fetch_none_with_params_calls)
        self.assertEquals(1, self.__conn.get_last_row_id_calls)

    def __GetTreasureIslandWithFormat(self, format_code):
        b = self.__GetTreasureIsland()
        bf = BookFormat()
        bf.Format = format_code
        b.formats.append(bf)
        return b

    @staticmethod
    def __GetTreasureIsland():
        b = Book()
        b.id = "1"
        b.title = "Treasure Island"
        b.author = "Robert Louis Stevenson"
        return b

