class Persistence(object):

    def search_books(self, search_term):
        raise NotImplementedError

    def get_book_details(self, book_id):
        raise NotImplementedError

    def add_book(self, book):
        raise NotImplementedError

    def add_book_type(self, book_type):
        raise NotImplementedError

    def get_book_type(self, book_type):
        raise NotImplementedError

    def list_books_by_first_letter(self, first_letter):
        raise NotImplementedError

    def get_book_by_title_and_author(self, book):
        raise NotImplementedError

    def add_book_format(self, book_id, book_format):
        raise NotImplementedError

    def format_exists(self, book_id, book_format):
        raise NotImplementedError