import unittest

from aquarius.objects.booktype import booktype


class TestBookType(unittest.TestCase):
    """unit tests for the BookType object"""
    def testHasFormatCode(self):
        """The object should contain a Format attribute"""
        book_type = booktype()
        self.assertEqual(True, hasattr(book_type, "Format"))
        
    def testHasMimeType(self):
        """The object should contain a MimeType attribute"""
        book_type = booktype()
        self.assertEqual(True, hasattr(book_type, "MimeType"))