from Config import Config
from aquarius.objects.Book import Book
from aquarius.objects.bookformat import bookformat
from aquarius.objects.booktype import booktype
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.Connection import Connection
from aquarius.persistence.sqlitepersistence.DatabaseCreation \
    import DatabaseCreation
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.AddBookType import AddBookType
from aquarius.persistence.sqlitepersistence.GetBookDetails \
    import GetBookDetails
from aquarius.persistence.sqlitepersistence.GetBookType \
    import GetBookType
from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook


class SqlitePersistence(object):

    def __init__(self):
        self.__config = Config()
        self.__bookSearch = SearchBook()
        self.__bookAdd = AddBook()
        self.__book_details = GetBookDetails()
        self.__add_book_type = AddBookType()
        self.__get_book_type = GetBookType()
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
            self.__get_book_type.get_book_type(format_code, conn)
   
    def list_books_by_first_letter(self, first_letter):
        sql = "SELECT b.Id, b.Title, b.Author FROM Book b WHERE Title LIKE '%s%s'" %\
              (first_letter, "%")

        with Connection(self.__config) as conn:
            return self.__convert_search_results_to_books(list(
                conn.execute_sql_fetch_all(sql)), conn)
        
    def __convert_search_results_to_books(self, search_result, conn):
        books = []        
        for result in search_result:
            self.__convert_search_result_to_book(books, result, conn)
        return books
    
    def __convert_search_result_to_book(self, books, result, conn):
        b = Book()
        b.id, b.title, b.author = result
        self.__add_formats_to_book(b, conn)
        books.append(b)
        
    def __add_formats_to_book(self, b, conn):
        formats = self.__get_formats_for_book(b, conn)
        for f in formats:
            self.__add_book_to_format(b, f)
    
    @staticmethod
    def __get_formats_for_book(b, conn):
        sql = "SELECT Format, Location FROM BookFormat WHERE Book=%s" % b.id
        formats = conn.execute_sql_fetch_all(sql)
        return formats
    
    @staticmethod
    def __add_book_to_format(b, book_format):
        bf = bookformat()
        bf.Format, bf.Location = book_format
        b.formats.append(bf)

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