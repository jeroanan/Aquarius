import xml.etree.ElementTree as etree

import uuid
from jinja2 import Environment, PackageLoader


class OpdsRequestHandler(object):

    def __init__(self, app, loader):
        self.__app = app
        self.__loader = loader

    def index_handler(self):
        return self.__loader.load_template("aquarius", "output/web/xml", "index.xml",
                                           feed_title="Aquarius EBook library")

    def by_title_handler(self):
        entries = []

        for i in range(0, 10):
            entries.append((str(i), "/firstletter/%s" % str(i), "Titles beginning with %s" % str(i)))

        for i in range(65, 91):
            entries.append((chr(i), "/firstletter/%s" % chr(i), "Titles beginning with %s" % chr(i)))

        return self.__loader.load_template("aquarius", "output/web/xml", "by_title.xml",
                                           feed_title="Browse books by title", entries=entries)

    def first_letter_handler(self, first_letter):
        books = self.__app.list_books_by_first_letter(first_letter)
        feed_title = "Titles beginning with %s" % first_letter
        return self.__loader.load_template("aquarius", "output/web/xml", "search_results.xml",
                                           feed_title=feed_title, books=books)

    def search_handler(self, search_term):
        books = self.__app.search_books(search_term)
        feed_title = "Search results for %s" % search_term
        return self.__loader.load_template("aquarius", "output/web/xml", "search_results.xml",
                                           feed_title=feed_title, books=books)

    def book_handler(self, book_id):
        book = self.__app.get_book_details(book_id)
        book_types = []

        for thisFormat in book.formats:
            book_types.append((thisFormat.Format, self.__app.get_book_type(thisFormat.Format)))

        return self.__loader.load_template("aquarius", "output/web/xml", "book.xml", book=book, book_types=book_types)

    def download_handler(self, book_id, book_format):
        book = self.__app.get_book_details(book_id)
        for thisFormat in book.formats:
            if thisFormat.Format == book_format:
                with open(thisFormat.Location, 'r') as f:
                    return f.read()
