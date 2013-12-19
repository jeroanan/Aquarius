import unittest
from unittest.mock import Mock

from config import config
from persistence.sqlitepersistence.addbook import addbook
from persistence.sqlitepersistence.searchbook import searchbook
from persistence.sqlitepersistence.sqlitepersistence import persistence

class sqlitepersistence_tests(unittest.TestCase):   

    def setUp(self):
        self.__setupConfigMock()
        self.__setupAddBookMock()
        self.__setupSearchBookMock()
    
    def __setupConfigMock(self):
        self.__config = config()
        self.__config.SqlLiteDatabasePath = "./database.db"

    def __setupAddBookMock(self):
        self.__addbook = addbook()
        self.__addbook.AddBook = Mock(return_value=None)

    def __setupSearchBookMock(self):
        self.__searchbook = searchbook()
        self.__searchbook.SearchBooks = Mock(return_value=None)
        self.__searchbook.GetBookDetails = Mock(return_value=None)
            
    def testSearchingBooksCausesTheSearchMethodToBeCalled(self):
        p = persistence(self.__config, self.__searchbook, self.__addbook)
        p.SearchBooks("Moo")
        self.assertTrue(self.__searchbook.SearchBooks.called)    
    
    def testCallingGetBookDetailsCausesTheGetBookDetailsMethodToBeCalled(self):
        p = persistence(self.__config, self.__searchbook, self.__addbook)
        p.GetBookDetails(1)
        self.assertTrue(self.__searchbook.GetBookDetails.called)
    
    def testCallingAddBookCausesTheAddBookMethodToBeCalled(self):
        p = persistence(self.__config, self.__searchbook, self.__addbook)
        p.AddBook(None)        
        self.assertTrue(self.__addbook.AddBook.called)