class GetBookDetailsInteractor(object):

    def __init__(self, persistence):
        self.__persistence = persistence

    def execute(self, param):
        return self.__persistence.get_book_details(param)