#!/usr/bin/python3

import unittest
from objects.book import book
from objects.bookformat import bookformat

class book_tests(unittest.TestCase):
    
    def setUp(self):
        self.b = book()
        
    def testSettingAuthorAttributeCausesAuthorToBeStored(self):
        self.b.Author = "An Author"
        self.assertEqual("An Author", self.b.Author)

    def testSettingTitleAttributeCausesTitleToBeStored(self):
        self.b.Title = "My Book"
        self.assertEqual("My Book", self.b.Title)
        
    def testSettingIdAttributeCausesIdToBeStored(self):
        self.b.Id = "1337"
        self.assertEqual("1337", self.b.Id)
        
    def testSettingFormatsAttributeCausesFormatsToBeStored(self):
        self.b.Formats = ["Format", "Epub"]
        self.assertEqual("Format", self.b.Formats[0])
        self.assertEqual("Epub", self.b.Formats[1])
                
    def testBooksMatchWhenTheyAreIdentical(self):        
        b1 = self.__getTreasureIsland()
        b2 = self.__getTreasureIsland()
        self.assertTrue(b1 == b2)
    
    def testBooksMatchWhenTheyAreIdenticalButMixedCase(self):
        b1 = self.__getTreasureIsland()
        b2 = self.__getTreasureIsland()
        b2.Title = str.lower(b2.Title)
        b2.Author = str.lower(b2.Author)
        self.assertTrue(b1 == b2)
    
    def testBooksDontMatchWhenTheyAreNotIdentical(self):
        b1 = self.__getTreasureIsland()    
        b2 = self.__getGreatExpectations()
        self.assertFalse(b1 == b2)
        
    def testAddingANewFormatCausesANewOneToBeStored(self):
        b = self.__getTreasureIsland()
        b.AddFormat(self.__getEPubFormart())
        self.assertEqual(1, len(b.Formats))
        
    def testAddingAnExistingFormatDoesNotCauseADuplicateToBeStored(self):
        b = self.__getTreasureIsland()
        b.AddFormat(self.__getEPubFormart())
        b.AddFormat(self.__getEPubFormart())
        self.assertEqual(1, len(b.Formats))
    
    def testToStringReturnsFormattedString(self):
        b = self.__getTreasureIsland()
        expected = "%s - %s" % (b.Author, b.Title)
        self.assertEqual(expected, str(b))
    
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
    
    def __getEPubFormart(self):
        bf = bookformat()
        bf.Format = "EPUB"
    
    