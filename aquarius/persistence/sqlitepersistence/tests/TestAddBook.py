import os
import unittest

from Config import Config
from aquarius.objects.Book import Book
from aquarius.objects.bookformat import bookformat
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.Connection import Connection
from aquarius.persistence.sqlitepersistence.ParameterSanitiser \
    import ParameterSanitiser
from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook
from aquarius.persistence.sqlitepersistence.SqlitePersistence import Persistence


class TestAddBook(unittest.TestCase):
    """Unit tests for the AddBook class"""
    def setUp(self):
        """Common test setup operations"""
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
        """Get a test book with a format"""
        b = self.__GetTreasureIsland()
        bf = bookformat()
        bf.Format = format_code
        b.formats.append(bf)
        return b

    @staticmethod
    def __GetTreasureIsland():
        """Provide details for the test book"""
        b = Book()
        b.id = "1"
        b.title = "Treasure Island"
        b.author = "Robert Louis Stevenson"
        return b

    def testCanSetParameterSanitiser(self):
        """Test that AddBook's parameter sanitiser can be set on-the-fly"""
        self.__add_book.set_parameter_sanitiser(None)


class ConnectionSpy(Connection):
    """Test double for the connection object"""

    def __init__(self):
        """Set initial object state"""
        self.fetch_all_calls = 0
        self.fetch_none_calls = 0
        self.get_last_row_id_calls = 0

    def execute_sql_fetch_all(self, sql):
        """spy on execute_sql_fetch_all"""
        self.fetch_all_calls += 1
        return []

    def execute_sql(self, sql):
        """spy on execute_sql"""
        self.fetch_none_calls += 1

    def get_last_row_id(self):
        """Spy on get_last_row_id"""
        self.get_last_row_id_calls += 1
        return 0


class ParameterSanitiserSpy(ParameterSanitiser):
    """Test double for ParameterSanitiser. Allows sensing of what
    gets called for that class when sql statements are being assembled"""
    def __init__(self):
        """Set initial object state"""
        self.sanitise_calls = 0

    def sanitise(self, args):
        """register that sanitise was called"""
        self.sanitise_calls += 1
        return args
