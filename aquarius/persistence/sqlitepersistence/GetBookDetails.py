from aquarius.objects.Book import Book
from aquarius.persistence.sqlitepersistence.BookFinder import BookFinder


class GetBookDetails(BookFinder):

    def __init__(self, connection):
        self.connection = connection

    def get_book_details(self, book_id):
        self.connection = self.connection
        sql = "SELECT Id, Title, Author FROM Book WHERE Id=?"
        b = Book()
        books = self.convert_search_results_to_books(self.connection.execute_sql_fetch_all_with_params(sql, (book_id,)))
        if len(books) > 0:
            b = books[0]
        return b
