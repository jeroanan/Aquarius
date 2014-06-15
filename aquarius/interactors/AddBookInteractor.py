from aquarius.Interactor import Interactor


class AddBookInteractor(Interactor):

    def __init__(self, persistence):
        self.__persistence = persistence

    def execute(self, book):
        book.id = self.__persistence.get_book_by_title_and_author(book).id
        if not self.__book_exists(book):
            self.__persistence.add_book(book)
            book.id = self.__persistence.get_book_by_title_and_author(book).id
        self.__add_book_formats(book)

    def __add_book_formats(self, b):
        for f in b.formats:
            if self.__format_does_not_exist(b, f.Format):
                self.__persistence.add_book_format(b.id, f)

    def __book_exists(self, book):
        return book.id != ""

    def __format_does_not_exist(self, book, book_format):
        return not self.__persistence.format_exists(book.id, book_format)