import unittest
from aquarius.objects.book import book
from aquarius.objects.bookformat import bookformat


class TestBook(unittest.TestCase):
    """Unit tests for the Book object"""
    def setUp(self):
        """Common setup operations"""
        self.b = book()
        
    def testSettingAuthorAttributeCausesAuthorToBeStored(self):
        """Give an author, then the book object stores it."""
        self.b.Author = "An Author"
        self.assertEqual("An Author", self.b.Author)

    def testSettingTitleAttributeCausesTitleToBeStored(self):
        """Given a book title, then the book object stores it."""
        self.b.Title = "My Book"
        self.assertEqual("My Book", self.b.Title)
        
    def testSettingIdAttributeCausesIdToBeStored(self):
        """Given a book Id, then the book object stores it."""
        self.b.Id = "1337"
        self.assertEqual("1337", self.b.Id)
        
    def testSettingFormatsAttributeCausesFormatsToBeStored(self):
        """Given book formats, then the object stores it."""
        self.b.Formats = ["Format", "Epub"]
        self.assertEqual("Format", self.b.Formats[0])
        self.assertEqual("Epub", self.b.Formats[1])
                
    def testBooksMatchWhenTheyAreIdentical(self):
        """Given another book object, when they have the same author and
        title, then they evaluate to be equal."""
        b1 = self.__getTreasureIsland()
        b2 = self.__getTreasureIsland()
        self.assertTrue(b1 == b2)
    
    def testBooksMatchWhenTheyAreIdenticalButMixedCase(self):
        """Given another book object, when they have the same author and title
        but they are of different case, then they evaluate to be equal."""
        b1 = self.__getTreasureIsland()
        b2 = self.__getTreasureIsland()
        b2.Title = str.lower(b2.Title)
        b2.Author = str.lower(b2.Author)
        self.assertTrue(b1 == b2)
    
    def testBooksDontMatchWhenTheyAreNotIdentical(self):
        """Given another book object, when they don't have the same
        author/title, then they do not evaluate to be equal"""
        b1 = self.__getTreasureIsland()    
        b2 = self.__getGreatExpectations()
        self.assertFalse(b1 == b2)
        
    def testAddingANewFormatCausesANewOneToBeStored(self):
        """Given a book format, it causes the book to add a new entry
        to its list of formats"""
        b = self.__getTreasureIsland()
        b.AddFormat(self.__getEPubFormat())
        self.assertEqual(1, len(b.Formats))
        
    def testAddingAnExistingFormatDoesNotCauseADuplicateToBeStored(self):
        """Given a book format, when the book already has that format, then
        a second entry for that format is not stored."""
        b = self.__getTreasureIsland()
        b.AddFormat(self.__getEPubFormat())
        b.AddFormat(self.__getEPubFormat())
        self.assertEqual(1, len(b.Formats))
    
    def testToStringReturnsFormattedString(self):
        """Given a request for the book object as a string, then the object
        returns a formatted string of author and title."""
        b = self.__getTreasureIsland()
        expected = "%s - %s" % (b.Author, b.Title)
        self.assertEqual(expected, str(b))
    
    @staticmethod
    def __getTreasureIsland():
        b = book()
        b.Author = "Robert Louis Stevenson"
        b.Title = "Treasure Island"
        return b
    
    @staticmethod
    def __getGreatExpectations():
        b = book()
        b.Author = "Charles Dickens"
        b.Author = "Great Expectations"
        return b 
    
    @staticmethod
    def __getEPubFormat():
        bf = bookformat()
        bf.Format = "EPUB"
