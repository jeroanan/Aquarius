import unittest
from aquarius.InteractorFactory import InteractorFactory


class TestInteractorFactory(unittest.TestCase):

    def setUp(self):
        self.__target = InteractorFactory()

    def test_get_add_book_interactor(self):
        self.__assertNotImplemented(self.__target.get_add_book_interactor)

    def test_get_list_books_by_first_letter_interactor(self):
        self.__assertNotImplemented(self.__target.get_list_books_by_first_letter_interactor)

    def test_get_search_book_interactor(self):
        self.__assertNotImplemented(self.__target.get_search_book_interactor)

    def test_get_book_details_interactor(self):
        self.__assertNotImplemented(self.__target.get_book_details_interactor)

    def __assertNotImplemented(self, method):
        self.assertRaises(NotImplementedError, method, "persistence")