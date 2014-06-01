from aquarius.InteractorFactory import InteractorFactory
from aquarius.interactors.AddBookInteractor import AddBookInteractor
from aquarius.interactors.GetBookDetailsInteractor import GetBookDetailsInteractor
from aquarius.interactors.GetBookTypeInteractor import GetBookTypeInteractor
from aquarius.interactors.ListBooksByFirstLetterInteractor import ListBooksByFirstLetterInteractor
from aquarius.interactors.SearchBookInteractor import SearchBookInteractor


class BasicInteractorFactory(InteractorFactory):

    def get_add_book_interactor(self, persistence):
        return AddBookInteractor(persistence)

    def get_list_books_by_first_letter_interactor(self, persistence):
        return ListBooksByFirstLetterInteractor(persistence)

    def get_search_book_interactor(self, persistence):
        return SearchBookInteractor(persistence)

    def get_book_details_interactor(self, persistence):
        return GetBookDetailsInteractor(persistence)

    def get_book_type_interactor(self, persistence):
        return GetBookTypeInteractor(persistence)