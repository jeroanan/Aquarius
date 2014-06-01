class InteractorFactory(object):

    def get_add_book_interactor(self, persistence):
        raise NotImplementedError

    def get_list_books_by_first_letter_interactor(self, persistence):
        raise NotImplementedError

    def get_search_book_interactor(self, persistence):
        raise NotImplementedError

    def get_book_details_interactor(self, param):
        raise NotImplementedError