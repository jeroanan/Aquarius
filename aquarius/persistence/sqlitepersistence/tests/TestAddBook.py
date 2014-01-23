import unittest

from aquarius.objects.Book import Book
from aquarius.objects.bookformat import bookformat
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.tests.Mocks.ConnectionSpy \
    import ConnectionSpy
from aquarius.persistence.sqlitepersistence.tests.Mocks.ParameterSanitiserSpy \
    import ParameterSanitiserSpy


class TestAddBook(unittest.TestCase):

    def setUp(self):
        self.__add_book = AddBook()
        self.__parameter_sanitiser = ParameterSanitiserSpy()
        self.__add_book.set_parameter_sanitiser(self.__parameter_sanitiser)
        self.__conn = ConnectionSpy()

    def testAddingBookWithOneFormatCausesTheCorrectDatabaseCalls(self):
        """Given a book to be added, when the book does not already exist
        in the database and has only one format, then add it and its format"""
        self.__add_book.add_book(self.__GetTreasureIslandWithFormat("EPUB"),
                                 self.__conn)
        self.assertEquals(2, self.__conn.fetch_all_calls)
        self.assertEqual(2, self.__conn.fetch_none_calls)
        self.assertEquals(1, self.__conn.get_last_row_id_calls)
        self.assertEquals(4, self.__parameter_sanitiser.sanitise_calls)

    def testAddingTwoIdenticalBooksCausesOnlyOneToBeWritten(self):
        """Given two books, when they're identical, then cause only one book
        to be added to the database."""
        b = self.__GetTreasureIsland()
        self.__add_book.add_book(b, self.__conn)
        self.assertEquals(1, self.__conn.fetch_all_calls)
        self.assertEqual(1, self.__conn.fetch_none_calls)
        self.assertEquals(1, self.__conn.get_last_row_id_calls)
        self.assertEquals(2, self.__parameter_sanitiser.sanitise_calls)

    def __GetTreasureIslandWithFormat(self, format_code):
        b = self.__GetTreasureIsland()
        bf = bookformat()
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

