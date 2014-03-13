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
        doc = self.__construct_common_header("Aquarius EBook Library")
        book = self.__app.get_book_details(book_id)
        self.__add_acquisition_details(book, doc)

        for thisFormat in book.formats:
            self.__add_acquisition_link(book, thisFormat.Format, doc)
        return doc

    def download_handler(self, book_id, book_format):
        book = self.__app.get_book_details(book_id)
        for thisFormat in book.formats:
            if thisFormat.Format == book_format:
                with open(thisFormat.Location, 'r') as f:
                    return f.read()

    def __construct_common_header(self, title):
        feed_element = etree.Element('feed', attrib={
            "xmlns": "http://www.w3.org/2005/Atom",
            "xmlns:opds": "http://opds-spec.org/2010/catalog"})
        etree.SubElement(feed_element, "id").text = str(uuid.uuid4())
        etree.SubElement(feed_element, "title").text = title
        etree.SubElement(feed_element, "link").attrib = {"href": "/search/{searchTerms}",
                                                        "type": "application/atom+xml",
                                                        "rel": "search",
                                                        "title": "Search"}
        return feed_element

    def __add_acquisition_details(self, book, doc):
        entry = etree.SubElement(doc, "entry")
        etree.SubElement(entry, "title").text = book.title

    def __add_acquisition_link(self, book, file_ext, doc):
        entry = doc.find("entry")
        book_type = self.__app.get_book_type(file_ext)

        e = etree.SubElement(entry, "link", attrib={
            "rel": "http://opds-spec.org/acquisition",
            "href": "/download/%s/%s" % (book.id, file_ext),
            "type": book_type.MimeType})
        author = etree.SubElement(e, "author")
        etree.SubElement(author, "name").text = book.author
        etree.SubElement(author, "uri").text = book.author_uri
