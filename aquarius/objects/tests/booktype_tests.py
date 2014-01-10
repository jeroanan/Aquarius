import unittest

from aquarius.objects.booktype import booktype


class booktype_tests(unittest.TestCase):
    
    def testHasFormatCode(self):
        bookType = booktype()
        self.assertEqual(True, hasattr(bookType, "Format"))
        
    def testHasMimeType(self):
        bookType = booktype()
        self.assertEqual(True, hasattr(bookType, "MimeType"))