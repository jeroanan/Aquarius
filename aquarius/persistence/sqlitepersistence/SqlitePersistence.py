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
        return self.__run_query(self.__query_factory.create_book_search, search_term)

    def get_book_details(self, book_id):
        return self.__run_query(self.__query_factory.create_get_book_details, book_id)

    def add_book(self, b):
        return self.__run_query(self.__query_factory.create_add_book, b)

    def add_book_type(self, book_type):
        return self.__run_query(self.__query_factory.create_add_book_type, book_type)

    def get_book_type(self, format_code):
        return self.__run_query(self.__query_factory.create_get_book_type, format_code)

    def list_books_by_first_letter(self, first_letter):
        self.__run_query(self.__query_factory.create_first_book_by_letter, first_letter)

    def get_book_by_title_and_author(self, book):
        self.__run_query(self.__query_factory.create_get_book_by_title_and_author, book)

    def add_book_format(self, book_id, book_format):
        self.__run_query(self.__query_factory.create_add_book_format, book_id, book_format)

    def format_exists(self, book_id, book_format):
        self.__run_query(self.__query_factory.create_format_exists, book_id, book_format)

    def __run_query(self, factory_method, *param):
        with Connection(self.__config) as conn:
            query = factory_method(conn)
            return query.execute(param)