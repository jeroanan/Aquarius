import unittest
from aquarius.objects.Book import Book
from aquarius.objects.bookformat import bookformat


class TestBook(unittest.TestCase):
    """Unit tests for the Book object"""
    def setUp(self):
        """Common setup operations"""
        self.b = Book()
        
    def testSettingAuthorAttributeCausesAuthorToBeStored(self):
        """Give an author, then the book object stores it."""
        self.b.author = "An Author"
        self.assertEqual("An Author", self.b.author)

    def testSettingTitleAttributeCausesTitleToBeStored(self):
        """Given a book title, then the book object stores it."""
        self.b.title = "My Book"
        self.assertEqual("My Book", self.b.title)
        
    def testSettingIdAttributeCausesIdToBeStored(self):
        """Given a book Id, then the book object stores it."""
        self.b.id = "1337"
        self.assertEqual("1337", self.b.id)
        
    def testSettingFormatsAttributeCausesFormatsToBeStored(self):
        """Given book formats, then the object stores it."""
        self.b.formats = ["Format", "Epub"]
        self.assertEqual("Format", self.b.formats[0])
        self.assertEqual("Epub", self.b.formats[1])
                
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
        b2.title = str.lower(b2.title)
        b2.author = str.lower(b2.author)
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
        b.add_format(self.__getEPubFormat())
        self.assertEqual(1, len(b.formats))
        
    def testAddingAnExistingFormatDoesNotCauseADuplicateToBeStored(self):
        """Given a book format, when the book already has that format, then
        a second entry for that format is not stored."""
        b = self.__getTreasureIsland()
        b.add_format(self.__getEPubFormat())
        b.add_format(self.__getEPubFormat())
        self.assertEqual(1, len(b.formats))
    
    def testToStringReturnsFormattedString(self):
        """Given a request for the book object as a string, then the object
        returns a formatted string of author and title."""
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
        bf = bookformat()
        bf.Format = "EPUB"
