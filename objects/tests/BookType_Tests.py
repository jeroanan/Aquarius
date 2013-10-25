import unittest

from objects.booktype import booktype

class BookType_Tests(unittest.TestCase):
    
    def testHasFormatCode(self):
        bookType = booktype()
        self.assertEqual(True, hasattr(bookType, "Format"))
        
    def testHasMimeType(self):
        bookType = booktype()
        self.assertEqual(True, hasattr(bookType, "MimeType"))