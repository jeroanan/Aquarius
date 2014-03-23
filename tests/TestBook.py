import unittest
from aquarius.objects.Book import Book
from aquarius.objects.BookFormat import BookFormat


class TestBook(unittest.TestCase):

    def setUp(self):
        self.b = Book()
        
    def test_setting_author_stores_author(self):
        self.b.author = "An Author"
        self.assertEqual("An Author", self.b.author)

    def test_setting_title_stores_title(self):
        self.b.title = "My Book"
        self.assertEqual("My Book", self.b.title)
        
    def test_setting_id_stores_id(self):
        self.b.id = "1337"
        self.assertEqual("1337", self.b.id)
        
    def test_setting_formats_stores_formats(self):
        self.b.formats = ["Format", "Epub"]
        self.assertEqual("Format", self.b.formats[0])
        self.assertEqual("Epub", self.b.formats[1])
                
    def test_equality_matching_books_is_true(self):
        b1 = self.__get_treasure_sland()
        b2 = self.__get_treasure_sland()
        self.assertTrue(b1 == b2)
    
    def test_equality_matching_books_mismatch_case_is_true(self):
        b1 = self.__get_treasure_sland()
        b2 = self.__get_treasure_sland()
        b2.title = str.lower(b2.title)
        b2.author = str.lower(b2.author)
        self.assertTrue(b1 == b2)
    
    def test_equality_mismatched_books_is_false(self):
        b1 = self.__get_treasure_sland()
        b2 = self.__get_great_expectations()
        self.assertFalse(b1 == b2)

    def test_equality_false_when_one_is_none(self):
        b1 = self.__get_treasure_sland()
        b2 = None
        self.assertFalse(b1 == b2)

    def test_adding_format_stores_format(self):
        b = self.__get_treasure_sland()
        b.add_format(self.__get_epub_format())
        self.assertEqual(1, len(b.formats))
        
    def test_adding_existing_format_does_not_store_it(self):
        b = self.__get_treasure_sland()
        b.add_format(self.__get_epub_format())
        b.add_format(self.__get_epub_format())
        self.assertEqual(1, len(b.formats))
    
    def test_to_string_returns_formatted_string(self):
        b = self.__get_treasure_sland()
        expected = "%s - %s" % (b.author, b.title)
        self.assertEqual(expected, str(b))
    
    @staticmethod
    def __get_treasure_sland():
        b = Book()
        b.author = "Robert Louis Stevenson"
        b.title = "Treasure Island"
        return b
    
    @staticmethod
    def __get_great_expectations():
        b = Book()
        b.author = "Charles Dickens"
        b.author = "Great Expectations"
        return b 
    
    @staticmethod
    def __get_epub_format():
        bf = BookFormat()
        bf.Format = "EPUB"
