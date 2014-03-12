import xml.etree.ElementTree as etree

import uuid


class OpdsRequestHandler(object):

    def __init__(self, app):
        self.__app = app

    def index_handler(self):
        doc = self.__construct_common_header("Aquarius EBook library")
        self.__add_index_entry("List By Letter", "Browse books by title", "/bytitle", doc)
        return doc

    def by_title_handler(self):
        doc = self.__construct_common_header("Browse books by title")

        for i in range(0, 10):
            self.__add_index_entry(str(i), "Titles beginning with %s" % str(i), "/firstletter/%s" % str(i), doc)

        for i in range(65, 91):
            self.__add_index_entry(chr(i), "Titles beginning with %s" % chr(i), "/firstletter/%s" % chr(i), doc)
        return doc

    def first_letter_handler(self, first_letter):
        doc = self.__construct_common_header("Titles beginning with %s" % first_letter)
        books = self.__app.list_books_by_first_letter(first_letter)

        for book in books:
            self.__add_book_index_entry(book, doc)
        return doc

    def book_handler(self, book_id):
        doc = self.__construct_common_header("Aquarius EBook Library")
        book = self.__app.get_book_details(book_id)
        self.__add_acquisition_details(book, doc)

        for thisFormat in book.formats:
            pass
            self.__add_acquisition_link(book, thisFormat.Format, doc)
        return doc

    def download_handler(self, book_id, book_format):
        book = self.__app.get_book_details(book_id)
        for thisFormat in book.formats:
            if thisFormat.Format == book_format:
                with open(thisFormat.Location, 'r') as f:
                    return f.read()

    def search_handler(self, search_term):
        doc = self.__construct_common_header("Search results for %s" % search_term)
        books = self.__app.search_books(search_term)
        for book in books:
            self.__add_book_index_entry(book, doc)
        return doc

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

    def __add_book_index_entry(self, book, doc):
        entry = etree.SubElement(doc, "entry")
        etree.SubElement(entry, "title").text = book.title
        etree.SubElement(entry, "link", attrib={"rel": "subsection",
                                                "href": "/book/%d" % book.id,
                                                "type": "application/atom+xml;profile=opds-catalog;kind=acquisition"})

        etree.SubElement(entry, "id").text = str(uuid.uuid4())
        etree.SubElement(entry, "content", attrib={"content": "text"}).text = book.author

    def __add_index_entry(self, title, description, href, doc):
        entry = etree.SubElement(doc, "entry")
        etree.SubElement(entry, "title").text = title
        etree.SubElement(entry, "link", attrib={"rel": "subsection",
                                                "href": href,
                                                "type": "application/atom+xml;profile=opds-catalog;kind=acquisition"})
        etree.SubElement(entry, "id").text = str(uuid.uuid4())
        etree.SubElement(entry, "content", attrib={"content": "text"}).text = description

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
