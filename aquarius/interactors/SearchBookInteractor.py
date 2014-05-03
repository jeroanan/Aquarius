class SearchBookInteractor(object):
    def __init__(self, persistence):
        self.__persistence = persistence

    def execute(self, search_term):
        return self.__persistence.search_books(search_term)
