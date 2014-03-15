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
        self.__bookSearch = SearchBook()
        self.__bookAdd = AddBook()
        self.__book_details = GetBookDetails()
        self.__add_book_type = AddBookType()
        self.__get_book_type = GetBookType()
        self.__list_books_by_first_letter = ListBooksByFirstLetter()

        DatabaseCreation(self.__config).create_db()
            
    def search_books(self, search_term):
        with Connection(self.__config) as conn:
            return self.__bookSearch.search_books(search_term, conn)
    
    def get_book_details(self, book_id):
        with Connection(self.__config) as conn:
            return self.__book_details.get_book_details(book_id, conn)
    
    def add_book(self, b):
        with Connection(self.__config) as conn:
            self.__bookAdd.add_book(b, conn)
    
    def add_book_type(self, book_type):
        with Connection(self.__config) as conn:
            self.__add_book_type.add_book_type(book_type, conn)

    def get_book_type(self, format_code):
        with Connection(self.__config) as conn:
            return self.__get_book_type.get_book_type(format_code, conn)
   
    def list_books_by_first_letter(self, first_letter):
        with Connection(self.__config) as conn:
            return self.__list_books_by_first_letter.list_books_by_first_letter(
                first_letter, conn)

    def set_add_book(self, add_book):
        self.__bookAdd = add_book

    def set_get_book_details(self, get_book_details):
        self.__book_details = get_book_details

    def set_book_search(self, book_search):
        self.__bookSearch = book_search

    def set_add_book_type(self, add_book_type):
        self.__add_book_type = add_book_type

    def set_get_book_type(self, get_book_type):
        self.__get_book_type = get_book_type

    def set_first_book_by_letter(self, list_first_book_by_letter):
        self.__list_books_by_first_letter = list_first_book_by_letter