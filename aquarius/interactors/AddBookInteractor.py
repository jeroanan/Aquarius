class AddBookInteractor(object):

    def __init__(self, persistence):
        self.__persistence = persistence

    def execute(self, book):
        self.__persistence.get_book_by_title_and_author(book)