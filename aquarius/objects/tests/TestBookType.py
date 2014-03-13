import unittest

from aquarius.objects.BookType import BookType


class TestBookType(unittest.TestCase):
    """unit tests for the BookType object"""
    def testHasFormatCode(self):
        """The object should contain a Format attribute"""
        book_type = BookType()
        self.assertEqual(True, hasattr(book_type, "Format"))
        
    def testHasMimeType(self):
        """The object should contain a MimeType attribute"""
        book_type = BookType()
        self.assertEqual(True, hasattr(book_type, "MimeType"))