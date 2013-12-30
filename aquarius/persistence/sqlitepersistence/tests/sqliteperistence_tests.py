import os
import unittest
from unittest.mock import Mock

from config import config
from aquarius.objects.booktype import booktype
from aquarius.persistence.sqlitepersistence.addbook import addbook
from aquarius.persistence.sqlitepersistence.searchbook import searchbook
from aquarius.persistence.sqlitepersistence.sqlitepersistence import persistence

class sqlitepersistence_tests(unittest.TestCase):   

    def setUp(self):        
        self.__setupConfigMock()
        self.__setupAddBookMock()
        self.__setupSearchBookMock()
        self.__p = persistence(self.__config, self.__searchbook, self.__addbook)
    
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
        
    def tearDown(self):
        os.remove(self.__config.SqlLiteDatabasePath)
            
    def testSearchingBooksCausesTheSearchMethodToBeCalled(self):
        self.__p.SearchBooks("Moo")
        self.assertTrue(self.__searchbook.SearchBooks.called)    
    
    def testCallingGetBookDetailsCausesTheGetBookDetailsMethodToBeCalled(self):
        self.__p.GetBookDetails(1)
        self.assertTrue(self.__searchbook.GetBookDetails.called)
    
    def testCallingAddBookCausesTheAddBookMethodToBeCalled(self):
        self.__p.AddBook(None)        
        self.assertTrue(self.__addbook.AddBook.called)

    def testGetBookTypeGetsRightBookFormatName(self):
        self.__p.AddBookType(self.__getSomeFormatBookType())
        self.assertEqual("SomeFormat", self.__p.GetBookType("SomeFormat").Format)
        
    def testGetBookTypeGetsRightMimeType(self):
        self.__p.AddBookType(self.__getSomeFormatBookType())
        bt = self.__p.GetBookType("SomeFormat")
        self.assertEqual("text/someformat", bt.MimeType)
            
    def __getSomeFormatBookType(self):
        bt = booktype()
        bt.Format = "SomeFormat"
        bt.MimeType = "text/someformat"
        return bt
    
    def testGetBookTypesReturnsNoneWhenBookTypeNotFound(self):
        self.assertIsNone(self.__p.GetBookType("DoesntExist"))
