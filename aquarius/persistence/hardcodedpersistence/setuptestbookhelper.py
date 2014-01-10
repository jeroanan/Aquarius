from aquarius.objects.book import book
from aquarius.objects.bookformat import bookformat

import os


class setuptestbookhelper(object):
       
    def __init__(self):
        self.__books = []
        
    def Setup(self):
        self.__books.append(self.__add_book_with_all_formats())
        self.__books.append(self.__add_book_with_no_formats())
        return self.__books

    def __add_book_with_all_formats(self):
        b = book()
        b.Id = 1
        b.Title = "The Book with no name"
        b.Author = "An Author"
        b.AuthorUri = "about:none"        
        b.Formats.append(self.__get_epub_format())
        b.Formats.append(self.__get_mobi_format())
        b.Formats.append(self.__get_pdf_format())
        return b
    
    @staticmethod
    def __add_book_with_no_formats():
        b = book()
        b.Id = 1
        b.Title = "Treasure Island"
        b.Author = "Robert Louis Stevenson"
        b.AuthorUri = "about:none"
        return b
    
    def __get_epub_format(self):
        return self.__get_format("EPUB")

    def __get_mobi_format(self):
        return self.__get_format("MOBI")
    
    def __get_pdf_format(self):
        return self.__get_format("PDF")
    
    @staticmethod
    def __get_format(formatCode):
        f = bookformat()
        f.Format = formatCode
        f.Location = "%s/1.%s" % (os.getcwd(), formatCode)
        return f



