from aquarius.objects.Book import Book
from aquarius.persistence.sqlitepersistence.BookFinder import BookFinder


class GetBookDetails(BookFinder):
    def __init__(self):
        self.connection = None
        self.sanitiser = None
        super().__init__()

    def get_book_details(self, book_id, connection):
        self.connection = connection
        (i,) = self.sanitiser.sanitise((book_id,))
        sql = "SELECT Id, Title, Author FROM Book WHERE Id=%s" % i
        b = Book()
        books = self.convert_search_results_to_books(connection.execute_sql_fetch_all(sql))
        if len(books) > 0:
            b = books[0]
        return b

    def set_parameter_sanitiser(self, sanitiser):
        self.sanitiser = sanitiser