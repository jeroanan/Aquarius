from aquarius.objects.Book import Book
from aquarius.objects.BookFormat import BookFormat

import os


class SetupTestBookHelper(object):
    """Set up books to be included in the hardcoded persistence"""

    def __init__(self):
        self.__books = []
        
    def setup(self):
        """Add books to the hardcoded persistence"""
        self.__books.append(self.__add_book_with_all_formats())
        self.__books.append(self.__add_book_with_no_formats())
        return self.__books

    def __add_book_with_all_formats(self):
        b = Book()
        b.id = 1
        b.title = "The Book with no name"
        b.author = "An Author"
        b.author_uri = "about:none"
        b.formats.append(self.__get_epub_format())
        b.formats.append(self.__get_mobi_format())
        b.formats.append(self.__get_pdf_format())
        return b
    
    @staticmethod
    def __add_book_with_no_formats():
        b = Book()
        b.id = 1
        b.title = "Treasure Island"
        b.author = "Robert Louis Stevenson"
        b.author_uri = "about:none"
        return b
    
    def __get_epub_format(self):
        return self.__get_format("EPUB")

    def __get_mobi_format(self):
        return self.__get_format("MOBI")
    
    def __get_pdf_format(self):
        return self.__get_format("PDF")
    
    @staticmethod
    def __get_format(format_code):
        f = BookFormat()
        f.Format = format_code
        f.Location = "%s/1.%s" % (os.getcwd(), format_code)
        return f



