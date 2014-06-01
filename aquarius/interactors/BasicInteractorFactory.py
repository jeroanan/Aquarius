from aquarius.InteractorFactory import InteractorFactory
from aquarius.interactors.AddBookInteractor import AddBookInteractor
from aquarius.interactors.GetBookDetailsInteractor import GetBookDetailsInteractor
from aquarius.interactors.GetBookTypeInteractor import GetBookTypeInteractor
from aquarius.interactors.ListBooksByFirstLetterInteractor import ListBooksByFirstLetterInteractor
from aquarius.interactors.SearchBookInteractor import SearchBookInteractor


class BasicInteractorFactory(InteractorFactory):

    def __init__(self, persistence):
        self.__persistence = persistence

    def get_add_book_interactor(self):
        return AddBookInteractor(self.__persistence)

    def get_list_books_by_first_letter_interactor(self):
        return ListBooksByFirstLetterInteractor(self.__persistence)

    def get_search_book_interactor(self):
        return SearchBookInteractor(self.__persistence)

    def get_book_details_interactor(self):
        return GetBookDetailsInteractor(self.__persistence)

    def get_book_type_interactor(self):
        return GetBookTypeInteractor(self.__persistence)