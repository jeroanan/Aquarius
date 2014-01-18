import os
import unittest

from Config import Config
from aquarius.objects.book import book
from aquarius.objects.bookformat import bookformat
from aquarius.persistence.sqlitepersistence.addbook import addbook
from aquarius.persistence.sqlitepersistence.connection import connection
from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook
from aquarius.persistence.sqlitepersistence.sqlitepersistence import persistence


class TestAddBook(unittest.TestCase):
    """Unit tests for the AddBook class"""
    #TODO: These are supposed to be unit tests. stop them from calling the db
    def setUp(self):
        self.__a = addbook()
        self.__conf = Config()
        self.__conf.sqllite_database_path = "./database.db"
        self.__conn = connection(self.__conf)
        self.__p = persistence(self.__conf, SearchBook(), addbook())
        
    def tearDown(self):
        os.remove(self.__conf.sqllite_database_path)
        
    def testAddingTwoIdenticalBooksCausesOnlyOneToBeWritten(self):
        b = self.__GetTreasureIsland()
        with connection(self.__conf) as conn:
            self.__a.AddBook(b, conn)
        r = self.__p.SearchBooks("Treasure")
        self.assertEqual(1, len(list(r)))
        
    def testAddingBookCausesItsFormatsToBeAdded(self):
        with connection(self.__conf) as conn:
            self.__a.AddBook(self.__GetTreasureIslandWithFormat("EPUB"), conn)
        r = self.__p.SearchBooks("Treasure")[0]
        self.assertEqual(1, len(r.Formats))
    
    def testAddingABookThenTheSameBookWithADifferentFormatCausesBothFormatsToBeAdded(self):
        with connection(self.__conf) as conn:        
            self.__a.AddBook(self.__GetTreasureIslandWithFormat("EPUB"), conn)
            self.__a.AddBook(self.__GetTreasureIslandWithFormat("MOBI"), conn)
        r = self.__p.SearchBooks("Treasure")[0]
        self.assertEqual(2, len(r.Formats))
        
    def __GetTreasureIslandWithFormat(self, formatCode):
        b = self.__GetTreasureIsland()
        bf = bookformat()
        bf.Format = formatCode
        b.Formats.append(bf)
        return b
    
    @staticmethod
    def __GetTreasureIsland():
        b = book()
        b.Id = "1"
        b.Title = "Treasure Island"
        b.Author = "Robert Louis Stevenson"
        return b     