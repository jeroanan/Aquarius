import unittest
from aquarius.objects.Book import Book
from aquarius.objects.BookFormat import BookFormat


class TestBook(unittest.TestCase):

    def setUp(self):
        self.b = Book()
        
    def testSettingAuthorAttributeCausesAuthorToBeStored(self):
        self.b.author = "An Author"
        self.assertEqual("An Author", self.b.author)

    def testSettingTitleAttributeCausesTitleToBeStored(self):
        self.b.title = "My Book"
        self.assertEqual("My Book", self.b.title)
        
    def testSettingIdAttributeCausesIdToBeStored(self):
        self.b.id = "1337"
        self.assertEqual("1337", self.b.id)
        
    def testSettingFormatsAttributeCausesFormatsToBeStored(self):
        self.b.formats = ["Format", "Epub"]
        self.assertEqual("Format", self.b.formats[0])
        self.assertEqual("Epub", self.b.formats[1])
                
    def testBooksMatchWhenTheyAreIdentical(self):
        b1 = self.__getTreasureIsland()
        b2 = self.__getTreasureIsland()
        self.assertTrue(b1 == b2)
    
    def testBooksMatchWhenTheyAreIdenticalButMixedCase(self):
        b1 = self.__getTreasureIsland()
        b2 = self.__getTreasureIsland()
        b2.title = str.lower(b2.title)
        b2.author = str.lower(b2.author)
        self.assertTrue(b1 == b2)
    
    def testBooksDontMatchWhenTheyAreNotIdentical(self):
        b1 = self.__getTreasureIsland()
        b2 = self.__getGreatExpectations()
        self.assertFalse(b1 == b2)

    def testBooksDontMatchWhentheSecondOneIsNull(self):
        b1 = self.__getTreasureIsland()
        b2 = None
        self.assertFalse(b1 == b2)

    def testAddingANewFormatCausesANewOneToBeStored(self):
        b = self.__getTreasureIsland()
        b.add_format(self.__getEPubFormat())
        self.assertEqual(1, len(b.formats))
        
    def testAddingAnExistingFormatDoesNotCauseADuplicateToBeStored(self):
        b = self.__getTreasureIsland()
        b.add_format(self.__getEPubFormat())
        b.add_format(self.__getEPubFormat())
        self.assertEqual(1, len(b.formats))
    
    def testToStringReturnsFormattedString(self):
        b = self.__getTreasureIsland()
        expected = "%s - %s" % (b.author, b.title)
        self.assertEqual(expected, str(b))
    
    @staticmethod
    def __getTreasureIsland():
        b = Book()
        b.author = "Robert Louis Stevenson"
        b.title = "Treasure Island"
        return b
    
    @staticmethod
    def __getGreatExpectations():
        b = Book()
        b.author = "Charles Dickens"
        b.author = "Great Expectations"
        return b 
    
    @staticmethod
    def __getEPubFormat():
        bf = BookFormat()
        bf.Format = "EPUB"
