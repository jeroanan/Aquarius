import os
import unittest

from Config import Config
from aquarius.objects.Book import Book
from aquarius.objects.bookformat import bookformat
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.Connection import Connection
from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook
from aquarius.persistence.sqlitepersistence.SqlitePersistence import Persistence


class TestAddBook(unittest.TestCase):
    """Unit tests for the AddBook class"""
    #TODO: These are supposed to be unit tests. stop them from calling the db
    def setUp(self):
        self.__a = AddBook()
        self.__conf = Config()
        self.__conf.sqllite_database_path = "./database.db"
        self.__conn = Connection(self.__conf)
        self.__p = Persistence(self.__conf, SearchBook(), AddBook())
        
    def tearDown(self):
        os.remove(self.__conf.sqllite_database_path)
        
    def testAddingTwoIdenticalBooksCausesOnlyOneToBeWritten(self):
        b = self.__GetTreasureIsland()
        with Connection(self.__conf) as conn:
            self.__a.add_book(b, conn)
        r = self.__p.search_books("Treasure")
        self.assertEqual(1, len(list(r)))
        
    def testAddingBookCausesItsFormatsToBeAdded(self):
        with Connection(self.__conf) as conn:
            self.__a.add_book(self.__GetTreasureIslandWithFormat("EPUB"), conn)
        r = self.__p.search_books("Treasure")[0]
        self.assertEqual(1, len(r.formats))
    
    def testAddingABookThenTheSameBookWithADifferentFormatCausesBothFormatsToBeAdded(self):
        with Connection(self.__conf) as conn:
            self.__a.add_book(self.__GetTreasureIslandWithFormat("EPUB"), conn)
            self.__a.add_book(self.__GetTreasureIslandWithFormat("MOBI"), conn)
        r = self.__p.search_books("Treasure")[0]
        self.assertEqual(2, len(r.formats))
        
    def __GetTreasureIslandWithFormat(self, formatCode):
        b = self.__GetTreasureIsland()
        bf = bookformat()
        bf.Format = formatCode
        b.formats.append(bf)
        return b
    
    @staticmethod
    def __GetTreasureIsland():
        b = Book()
        b.id = "1"
        b.title = "Treasure Island"
        b.author = "Robert Louis Stevenson"
        return b     