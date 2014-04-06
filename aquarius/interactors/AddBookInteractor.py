class AddBookInteractor(object):

    def __init__(self, persistence):
        self.__persistence = persistence

    def execute(self, book):
        b = self.__persistence.get_book_by_title_and_author(book)
        if b.id == "":
            self.__persistence.add_book(book)
