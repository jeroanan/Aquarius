from aquarius.objects.BookFormat import BookFormat

import unittest


class TestBookFormat(unittest.TestCase):

    def setUp(self):
        self.format = BookFormat()
        return format

    def test_setting_location_stores_location(self):
        self.format.Location = "/dev/null"
        self.assertEqual("/dev/null", self.format.Location)
        
    def test_equality_matching_formats_is_true(self):
        f1 = self.__get_epub_format()
        f2 = self.__get_epub_format()
        self.assertTrue(f1 == f2)

    def test_equality_mismatched_casing_is_true(self):
        f1 = self.__get_epub_format()
        f2 = self.__get_epub_format()
        f2.Format = str.lower(f2.Format)
        self.assertTrue(f1 == f2)

    def test_equality_mismatched_formats_is_false(self):
        f1 = self.__get_epub_format()
        f2 = self.__get_pdf_format()
        self.assertFalse(f1 == f2)
        
    def __get_epub_format(self):
        return self.__get_format("EPUB")

    def __get_pdf_format(self):
        return self.__get_format("PDF")

    def __get_format(self, formatcode):
        f2 = BookFormat()
        f2.Format = formatcode
        return f2
