import unittest

from aquarius.objects.BookType import BookType


class TestBookType(unittest.TestCase):

    def test_booktype_has_format_attr(self):
        book_type = BookType()
        self.assertEqual(True, hasattr(book_type, "Format"))
        
    def test_booktype_has_mimetype_attr(self):
        book_type = BookType()
        self.assertEqual(True, hasattr(book_type, "MimeType"))