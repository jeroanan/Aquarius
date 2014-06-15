class GetBookTypeInteractor(object):

    def __init__(self, persistence):
        self.__persistence = persistence

    def execute(self, format_code):
        return self.__persistence.get_book_type(format_code)