from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.AddBookFormat import AddBookFormat
from aquarius.persistence.sqlitepersistence.AddBookType import AddBookType
from aquarius.persistence.sqlitepersistence.FormatExists import FormatExists
from aquarius.persistence.sqlitepersistence.GetBookByTitleAndAuthor import GetBookByTitleAndAuthor
from aquarius.persistence.sqlitepersistence.GetBookDetails import GetBookDetails
from aquarius.persistence.sqlitepersistence.GetBookType import GetBookType
from aquarius.persistence.sqlitepersistence.ListBooksByFirstLetter import ListBooksByFirstLetter
from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook


class QueryFactory(object):

    def create_add_book(self, connection):
        return AddBook(connection)

    def create_get_book_details(self, connection):
        return GetBookDetails(connection)

    def create_book_search(self, connection):
        return SearchBook(connection)

    def create_add_book_type(self, connection):
        return AddBookType(connection)

    def create_get_book_type(self, connection):
        return GetBookType(connection)

    def create_first_book_by_letter(self, connection):
        return ListBooksByFirstLetter(connection)

    def create_get_book_by_title_and_author(self, connection):
        return GetBookByTitleAndAuthor(connection)

    def create_add_book_format(self, connection):
        return AddBookFormat(connection)

    def create_format_exists(self, connection):
        return FormatExists(connection)