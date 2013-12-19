import unittest

from persistence.sqlitepersistence.sqlitepersistence import persistence

class sqlitepersistence_tests(unittest.TestCase):
    
    def testSearchingBooksCausesTheSearchMethodToBeCalled(self):
        s = searchbook_mock()
        p = persistence(config_mock(), s, addbook_mock())
        p.SearchBooks("Moo")
        self.assertEqual(1, s.searchCount)    
    
    def testCallingGetBookDetailsCausesTheGetBookDetailsMethodToBeCalled(self):
        s = searchbook_mock()
        p = persistence(config_mock(), s, addbook_mock())
        p.GetBookDetails(1)
        self.assertEqual(1, s.getBookDetailsCount)
    
    def testCallingAddBookCausesTheAddBookMethodToBeCalled(self):
        a = addbook_mock()
        p = persistence(config_mock(), searchbook_mock(), a)
        p.AddBook(None)
        self.assertEqual(1, a.addBookCount)
        
class config_mock(object):
    
    def __init__(self):
        self.SqlLiteDatabasePath = "./database.db" 
        
class addbook_mock(object):
    
    def __init__(self):
        self.addBookCount = 0
        
    def AddBook(self, book, config):
        self.addBookCount += 1
        
class searchbook_mock(object):
    
    def __init__(self):
        self.searchCount = 0
        self.getBookDetailsCount = 0
    
    def SearchBooks(self, searchTerm, conn):
        self.searchCount += 1
        
    def GetBookDetails(self, bookId):
        self.getBookDetailsCount += 1
