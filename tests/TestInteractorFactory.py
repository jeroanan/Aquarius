import unittest
from aquarius.InteractorFactory import InteractorFactory


class TestInteractorFactory(unittest.TestCase):

    def setUp(self):
        self.__f = InteractorFactory()

    def test_get_add_book_interactor(self):
        self.assertRaises(NotImplementedError, self.__f.get_add_book_interactor, "persistence")

    def test_get_list_books_by_first_letter_interactor(self):
        self.assertRaises(NotImplementedError, self.__f.get_list_books_by_first_letter_interactor, "persistence")

    def test_get_search_book_interactor(self):
        self.assertRaises(NotImplementedError, self.__f.get_search_book_interactor, "persistence")