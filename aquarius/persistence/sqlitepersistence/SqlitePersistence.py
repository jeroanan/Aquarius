from aquarius.objects.Book import Book
from aquarius.objects.bookformat import bookformat
from aquarius.objects.booktype import booktype
from aquarius.persistence.sqlitepersistence.AddBook import AddBook
from aquarius.persistence.sqlitepersistence.Connection import Connection
from aquarius.persistence.sqlitepersistence.DatabaseCreation import DatabaseCreation
from aquarius.persistence.sqlitepersistence.SearchBook import SearchBook


class SqlitePersistence(object):

    @staticmethod
    def get_instance(config):
        return Persistence(config, SearchBook(), AddBook())


class Persistence(object):

    def __init__(self, config, book_search, book_add):
        self.__bookSearch = book_search
        self.__bookAdd = book_add
        self.__config = config
        DatabaseCreation(config).create_db()
            
    def search_books(self, search_term):
        with Connection(self.__config) as conn:
            return self.__bookSearch.search_books(search_term, conn)
    
    def get_book_details(self, book_id):
        with Connection(self.__config) as conn:
            return self.__bookSearch.get_book_details(book_id, conn)
    
    def add_book(self, b):
        with Connection(self.__config) as conn:
            self.__bookAdd.add_book(b, conn)
    
    def add_book_type(self, book_type):
        sql = "INSERT INTO FORMAT (Code, MimeType) VALUES ('%s', '%s')" % \
              (book_type.Format, book_type.MimeType)
        with Connection(self.__config) as conn:
            conn.execute_sql(sql)
    
    def get_book_type(self, format_code):
        sql = "SELECT Code, MimeType FROM Format WHERE Code='%s'" % format_code
        with Connection(self.__config) as conn:
            r = conn.execute_sql_fetch_all(sql)
        if len(r) > 0:       
            bt = booktype()
            bt.Format = r[0][0]
            bt.MimeType = r[0][1]
            return bt
   
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
