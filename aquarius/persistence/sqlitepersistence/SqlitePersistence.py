from Config import Config
from aquarius.Persistence import Persistence
from aquarius.persistence.sqlitepersistence.Connection import Connection
from aquarius.persistence.sqlitepersistence.DatabaseCreation import DatabaseCreation


class SqlitePersistence(Persistence):

    def __init__(self, query_factory):
        self.__config = Config()
        self.__query_factory = query_factory
        DatabaseCreation(self.__config).create_db()
            
    def search_books(self, search_term):
        with Connection(self.__config) as conn:
            search = self.__query_factory.create_book_search(conn)
            return search.search_books(search_term)
    
    def get_book_details(self, book_id):
        with Connection(self.__config) as conn:
            book_details = self.__query_factory.create_get_book_details(conn)
            return book_details.get_book_details(book_id)
    
    def add_book(self, b):
        with Connection(self.__config) as conn:
            book_add = self.__query_factory.create_add_book(conn)
            book_add.add_book(b)
    
    def add_book_type(self, book_type):
        with Connection(self.__config) as conn:
            add_book_type = self.__query_factory.create_add_book_type(conn)
            add_book_type.add_book_type(book_type)

    def get_book_type(self, format_code):
        with Connection(self.__config) as conn:
            get_book_type = self.__query_factory.create_get_book_type(conn)
            return get_book_type.get_book_type(format_code)
   
    def list_books_by_first_letter(self, first_letter):
        with Connection(self.__config) as conn:
            obj = self.__query_factory.create_first_book_by_letter(conn)
            return obj.list_books_by_first_letter(first_letter)

    def get_book_by_title_and_author(self, book):
        with Connection(self.__config) as conn:
            get_book_by_title_and_author = self.__query_factory.create_get_book_by_title_and_author(conn)
            return get_book_by_title_and_author.execute(book)

    def add_book_format(self, book_id, book_format):
        with Connection(self.__config) as conn:
            get_add_book_format = self.__query_factory.create_add_book_format(conn)
            get_add_book_format.execute(book_id, book_format)

    def format_exists(self, book_id, book_format):
        with Connection(self.__config) as conn:
            format_exists = self.__query_factory.create_format_exists(conn)
            return format_exists.execute(book_id, book_format)

