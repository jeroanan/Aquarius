from aquarius.objects.Book import Book
from aquarius.objects.BookFormat import BookFormat


class ListBooksByFirstLetter():

    def __init__(self, connection):
        self.__connection = connection

    def list_books_by_first_letter(self, first_letter):
        sql = "SELECT b.Id, b.Title, b.Author FROM Book b WHERE Title LIKE ?"
        result = self.__connection.execute_sql_fetch_all_with_params(sql, (list(first_letter)[0] + "%",))
        return self.__convert_search_results_to_books(list(result))

    def __convert_search_results_to_books(self, search_result):
        books = []
        for result in search_result:
            self.__convert_search_result_to_book(books, result)
        return books

    def __convert_search_result_to_book(self, books, result):
        b = Book()
        b.id, b.title, b.author = result
        self.__add_formats_to_book(b)
        books.append(b)

    def __add_formats_to_book(self, b):
        formats = self.__get_formats_for_book(b)
        for f in formats:
            self.__add_book_to_format(b, f)

    def __get_formats_for_book(self, b):
        sql = "SELECT Format, Location FROM BookFormat WHERE Book=?"
        formats = self.__connection.execute_sql_fetch_all_with_params(sql, (b.id,))
        return formats

    def __add_book_to_format(self, b, book_format):
        bf = BookFormat()
        bf.Format, bf.Location = book_format
        b.formats.append(bf)