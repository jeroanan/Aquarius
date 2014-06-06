import unittest
from aquarius.Persistence import Persistence

from aquarius.objects.Book import Book
from aquarius.objects.BookFormat import BookFormat
from aquarius.persistence.hardcodedpersistence.HardcodedPersistence import HardcodedPersistence


class TestHardcodedPersistence(unittest.TestCase):

    def setUp(self):
        self.p = HardcodedPersistence(None)
        
    def test_search_books_no_results(self):
        result = self.p.search_books("Don't find me")
        self.assertEqual(0, self.__count_books(result))

    def test_search_books_with_results(self):
        result = self.p.search_books("oo")
        self.assertEqual(1, self.__count_books(result))
    
    def test_search_books_empty_string(self):
        result = self.p.search_books("")
        self.assertEqual(0, self.__count_books(result))
        
    def test_list_books_by_first_letter_none_found(self):
        result = self.p.list_books_by_first_letter("p")
        self.assertEqual(0, self.__count_books(result))
    
    def test_list_books_by_first_letter_results_found(self):
        result = self.p.list_books_by_first_letter("t")
        self.assertEqual(2, self.__count_books(result))
        
    def test_get_book_details_book_doesnt_exist(self):
        result = self.p.get_book_details("-1")
        self.assertEqual(None, result)
        
    def test_get_book_details_book_exists(self):
        result = self.p.get_book_details("1")
        self.assertEqual(1, result.id)
    
    def test_get_book_type_doesnt_exist(self):
        t = self.p.get_book_type("exe")
        self.assertEqual(None, t)
        
    def test_get_book_type_exists(self):
        t = self.p.get_book_type("EPUB")
        self.assertEqual("EPUB", t.Format)
        
    def test_add_book_different_formats_just_one_instance_of_book_exists(self):
        self.p.add_book(self.__get_fly_fishing("EPUB"))
        self.p.add_book(self.__get_fly_fishing("MOBI"))
        self.__check_fly_fishing_book_count(1)
        self.__check_fishing_formats(2)
        
    def test_add_duplicate_book_does_not_add_second_format(self):
        self.p.add_book(self.__get_fly_fishing("EPUB"))
        self.p.add_book(self.__get_fly_fishing("EPUB"))
        self.__check_fishing_formats(1)

    def test_implements_persistence(self):
        self.assertIsInstance(self.p, Persistence)

    def __get_fly_fishing(self, formatcode):
        b = Book()
        b.title = "Fly Fishing"
        b.author = "J. R. Hartley"
        b.add_format(self.__get_format(formatcode))
        return b
    
    def __check_fishing_formats(self, expected):
        result = self.p.search_books("Fishing")
        self.assertEqual(expected, self.__count_formats(result))
    
    def __check_fly_fishing_book_count(self, expected):
        result = self.p.search_books("Fishing")
        self.assertEqual(expected, self.__count_books(result))

    def __get_format(self, formatcode):
        f = BookFormat()
        f.Format = formatcode
        return f

    def __count_books(self, result):
        return len(list(result))        

    def __count_formats(self, result):
        i = 0
        for b in result:
            i += len(list(b.formats))
        return i
