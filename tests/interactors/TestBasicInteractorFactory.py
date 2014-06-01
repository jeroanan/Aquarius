import unittest
from aquarius.interactors.BasicInteractorFactory import BasicInteractorFactory
from aquarius.interactors.GetBookDetailsInteractor import GetBookDetailsInteractor
from aquarius.interactors.SearchBookInteractor import SearchBookInteractor
from aquarius.interactors.AddBookInteractor import AddBookInteractor
from aquarius.interactors.ListBooksByFirstLetterInteractor import ListBooksByFirstLetterInteractor


class TestBasicInteractorFactory(unittest.TestCase):

    def setUp(self):
        self.__target = BasicInteractorFactory()

    def test_get_add_book_interactor(self):
        i = self.__target.get_add_book_interactor("persistence")
        self.assertIsInstance(i, AddBookInteractor)

    def test_get_list_books_by_first_letter_interactor(self):
        i = self.__target.get_list_books_by_first_letter_interactor("persistence")
        self.assertIsInstance(i, ListBooksByFirstLetterInteractor)

    def test_get_search_book_interactor(self):
        i = self.__target.get_search_book_interactor("persistence")
        self.assertIsInstance(i, SearchBookInteractor)

    def test_get_get_book_details_interactor(self):
        i = self.__target.get_book_details_interactor("persistence")
        self.assertIsInstance(i, GetBookDetailsInteractor)