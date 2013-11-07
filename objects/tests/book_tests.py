#!/usr/bin/python3

import unittest
from objects.book import book

class book_tests(unittest.TestCase):
    
    def setUp(self):
        self.b = book()
        
    def testHasAuthorAttribute(self):
        self.assertEqual(True, hasattr(self.b, "Author"))

    def testHasTitleAttribute(self):
        self.assertEqual(True, hasattr(self.b, "Title"))
        
    def testHasFormatsAttribute(self):
        self.assertTrue(hasattr(self.b, "Formats"))
    
    def testHasIdAttribute(self):
        self.assertTrue(hasattr(self.b, "Id"))
    
    def testSetAuthorAttribute(self):
        self.b.Author = "An Author"
        self.assertEqual("An Author", self.b.Author)

    def testSetTitle(self):
        self.b.Title = "My Book"
        self.assertEqual("My Book", self.b.Title)
        
    def testSetIdAttribute(self):
        self.b.Id = "1337"
        self.assertEqual("1337", self.b.Id)
        
    def testSetFormatsAttribute(self):
        self.b.Formats = ["Format", "Epub"]
        self.assertEqual("Format", self.b.Formats[0])
        self.assertEqual("Epub", self.b.Formats[1])
                
    def testEqualsBooksMatch(self):        
        b1 = self.__getTreasureIsland()
        b2 = self.__getTreasureIsland()
        self.assertTrue(b1 == b2)
    
    def testEqualsBooksDontMatch(self):
        b1 = self.__getTreasureIsland()    
        b2 = self.__getGreatExpectations()
        self.assertFalse(b1 == b2)
        
    def __getTreasureIsland(self):
        b = book()
        b.Author = "Robert Louis Stevenson"
        b.Title = "Treasure Island"
        return b
    
    def __getGreatExpectations(self):
        b = book()
        b.Author = "Charles Dickens"
        b.Author = "Great Expectations"
        return b 