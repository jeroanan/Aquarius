from aquarius.Interactor import Interactor


class AddBookInteractor(Interactor):

    def __init__(self, persistence):
        self.__persistence = persistence

    def execute(self, book):
        b = self.__persistence.get_book_by_title_and_author(book)
        if not self.__book_exists(b):
            self.__persistence.add_book(book)
            b = self.__persistence.get_book_by_title_and_author(book)
        self.__add_book_formats(b)

    def __add_book_formats(self, b):
        for f in b.formats:
            if self.__format_does_not_exist(b, f):
                self.__persistence.add_book_format(b.id, f)

    def __book_exists(self, book):
        return book.id != ""

    def __format_does_not_exist(self, book, book_format):
        return not self.__persistence.format_exists(book.id, book_format)