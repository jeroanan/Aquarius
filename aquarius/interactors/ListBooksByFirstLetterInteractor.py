from aquarius.Interactor import Interactor


class ListBooksByFirstLetterInteractor(Interactor):

    def __init__(self, persistence):
        self.__persistence = persistence

    def execute(self, first_letter):
        self.__persistence.list_books_by_first_letter(first_letter)