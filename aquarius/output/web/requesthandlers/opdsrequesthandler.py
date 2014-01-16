import xml.etree.ElementTree as etree

import uuid


class opdsrequesthandler(object):
    """Handles http requests made my an opds-enabled client."""
    def __init__(self, app):
        self.__app = app

    def IndexHandler(self):
        """Handles index page requests"""
        doc = self.__construct_common_header("Aquarius EBook library")
        self.__add_index_entry("List By Letter", "Browse books by title", "/bytitle", doc)
        return doc

    def ByTitleHandler(self):
        """Handles first letter page requests"""
        doc = self.__construct_common_header("Browse books by title")

        for i in range(0, 10):
            self.__add_index_entry(str(i), "Titles beginning with %s" % str(i), "/firstletter/%s" % str(i), doc)

        for i in range(65, 91):
            self.__add_index_entry(chr(i), "Titles beginning with %s" % chr(i), "/firstletter/%s" % chr(i), doc)
        return doc

    def FirstLetterHandler(self, firstletter):
        """Handles requests for books starting with the given letter"""
        doc = self.__construct_common_header("Titles beginning with %s" % firstletter)
        books = self.__app.ListBooksByFirstLetter(firstletter)

        for book in books:
            self.__add_book_index_entry(book, doc)
        return doc

    def BookHandler(self, book_id):
        """Handles requests for details of a specific book"""
        doc = self.__construct_common_header("Aquarius EBook Library")
        book = self.__app.GetBookDetails(book_id)
        self.__add_acquisition_details(book, doc)

        for thisFormat in book.Formats:
            pass
            self.__add_acquisition_link(book, thisFormat.Format, doc)
        return doc

    def DownloadHandler(self, book_id, book_format):
        """handles requests for the download of a book"""
        book = self.__app.GetBookDetails(book_id)
        for thisFormat in book.Formats:
            if thisFormat.Format == book_format:
                with open(thisFormat.Location, 'r') as f:
                    return f.read()

    def Search(self, search_term):
        """Handles book search requests"""
        doc = self.__construct_common_header("Search results for %s" % search_term)
        books = self.__app.SearchBooks(search_term)
        for book in books:
            self.__add_book_index_entry(book, doc)
        return doc

    @staticmethod
    def __construct_common_header(title):
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

    @staticmethod
    def __add_book_index_entry(book, doc):
        entry = etree.SubElement(doc, "entry")
        etree.SubElement(entry, "title").text = book.Title
        etree.SubElement(entry, "link", attrib={"rel": "subsection",
                                                "href": "/book/%d" % book.Id,
                                                "type": "application/atom+xml;profile=opds-catalog;kind=acquisition"})

        etree.SubElement(entry, "id").text = str(uuid.uuid4())
        etree.SubElement(entry, "content", attrib={"content": "text"}).text = book.Author

    @staticmethod
    def __add_index_entry(title, description, href, doc):
        entry = etree.SubElement(doc, "entry")
        etree.SubElement(entry, "title").text = title
        etree.SubElement(entry, "link", attrib={"rel": "subsection",
                                                "href": href,
                                                "type": "application/atom+xml;profile=opds-catalog;kind=acquisition"})
        etree.SubElement(entry, "id").text = str(uuid.uuid4())
        etree.SubElement(entry, "content", attrib={"content": "text"}).text = description

    @staticmethod
    def __add_acquisition_details(book, doc):
        entry = etree.SubElement(doc, "entry")
        etree.SubElement(entry, "title").text = book.Title

    def __add_acquisition_link(self, book, file_ext, doc):
        entry = doc.find("entry")
        book_type = self.__app.GetBookType(file_ext)

        e = etree.SubElement(entry, "link", attrib={
            "rel": "http://opds-spec.org/acquisition",
            "href": "/download/%s/%s" % (book.Id, file_ext),
            "type": book_type.MimeType})
        author = etree.SubElement(e, "author")
        etree.SubElement(author, "name").text = book.Author
        etree.SubElement(author, "uri").text = book.AuthorUri
