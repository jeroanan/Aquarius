from aquarius.objects.Book import Book
from aquarius.persistence.sqlitepersistence.BookFinder import BookFinder


class GetBookDetails(BookFinder):
    def __init__(self):
        self.connection = None
        self.sanitiser = None

    def get_book_details(self, book_id, connection):
        self.connection = connection
        sql = "SELECT Id, Title, Author FROM Book WHERE Id=?"
        b = Book()
        books = self.convert_search_results_to_books(connection.execute_sql_fetch_all_with_params(sql, (book_id,)))
        if len(books) > 0:
            b = books[0]
        return b
