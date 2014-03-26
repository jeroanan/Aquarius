from Config import Config
from aquarius.persistence.sqlitepersistence.Connection import Connection
from aquarius.persistence.sqlitepersistence.DatabaseCreation import DatabaseCreation
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.AddBookType import AddBookType
from aquarius.persistence.sqlitepersistence.GetBookDetails import GetBookDetails
from aquarius.persistence.sqlitepersistence.GetBookType import GetBookType
from aquarius.persistence.sqlitepersistence.ListBooksByFirstLetter import ListBooksByFirstLetter
from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook


class SqlitePersistence(object):

    def __init__(self):
        self.__config = Config()
        DatabaseCreation(self.__config).create_db()
            
    def search_books(self, search_term):
        with Connection(self.__config) as conn:
            search = self.get_book_search(conn)
            return search.search_books(search_term)
    
    def get_book_details(self, book_id):
        with Connection(self.__config) as conn:
            book_details = self.get_get_book_details(conn)
            return book_details.get_book_details(book_id)
    
    def add_book(self, b):
        with Connection(self.__config) as conn:
            book_add = self.get_add_book(conn)
            book_add.add_book(b)
    
    def add_book_type(self, book_type):
        with Connection(self.__config) as conn:
            add_book_type = self.get_add_book_type(conn)
            add_book_type.add_book_type(book_type)

    def get_book_type(self, format_code):
        with Connection(self.__config) as conn:
            get_book_type = self.get_get_book_type(conn)
            return get_book_type.get_book_type(format_code)
   
    def list_books_by_first_letter(self, first_letter):
        with Connection(self.__config) as conn:
            obj = self.get_first_book_by_letter(conn)
            return obj.list_books_by_first_letter(first_letter)

    def get_add_book(self, connection):
        return AddBook(connection)

    def get_get_book_details(self, connection):
        return GetBookDetails(connection)

    def get_book_search(self, connection):
        return SearchBook(connection)

    def get_add_book_type(self, connection):
        return AddBookType(connection)

    def get_get_book_type(self, connection):
        return GetBookType(connection)

    def get_first_book_by_letter(self, connection):
        return ListBooksByFirstLetter(connection)