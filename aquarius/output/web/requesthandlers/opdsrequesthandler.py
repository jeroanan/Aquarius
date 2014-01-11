import xml.etree.ElementTree as etree

import uuid


class opdsrequesthandler(object):
    def __init__(self, app):
        self.__app = app

    def IndexHandler(self):
        doc = self.__construct_common_header("Aquarius EBook library")
        self.__add_index_entry("List By Letter", "Browse books by title", "/bytitle", doc)
        return doc

    def ByTitleHandler(self):
        doc = self.__construct_common_header("Browse books by title")

        for i in range(0, 10):
            self.__add_index_entry(str(i), "Titles beginning with %s" % str(i), "/firstletter/%s" % str(i), doc)

        for i in range(65, 91):
            self.__add_index_entry(chr(i), "Titles beginning with %s" % chr(i), "/firstletter/%s" % chr(i), doc)
        return doc

    def FirstLetterHandler(self, firstletter):
        doc = self.__construct_common_header("Titles beginning with %s" % firstletter)
        books = self.__app.ListBooksByFirstLetter(firstletter)

        for book in books:
            self.__add_book_index_entry(book, "", doc)
        return doc

    def BookHandler(self, bookId):
        doc = self.__construct_common_header("Aquarius EBook Library")
        book = self.__app.GetBookDetails(bookId)
        self.__add_acquisiton_details(book, doc)

        for thisFormat in book.Formats:
            pass
            self.__add_acquisition_link(book, thisFormat.Format, doc)
        return doc

    def DownloadHandler(self, bookId, bookFormat):
        book = self.__app.GetBookDetails(bookId)
        for thisFormat in book.Formats:
            if thisFormat.Format == bookFormat:
                with open(thisFormat.Location, 'r') as f:
                    return f.read()

    def Search(self, searchTerm):
        doc = self.__construct_common_header("Search results for %s" % searchTerm)
        books = self.__app.SearchBooks(searchTerm)
        for book in books:
            self.__add_book_index_entry(book, "", doc)
        return doc

    @staticmethod
    def __construct_common_header(title):
        feedElement = etree.Element('feed', attrib={
            "xmlns": "http://www.w3.org/2005/Atom",
            "xmlns:opds": "http://opds-spec.org/2010/catalog"})
        etree.SubElement(feedElement, "id").text = str(uuid.uuid4())
        etree.SubElement(feedElement, "title").text = title
        etree.SubElement(feedElement, "link").attrib = {"href": "/search/{searchTerms}",
                                                        "type": "application/atom+xml",
                                                        "rel": "search",
                                                        "title": "Search"}
        return feedElement

    @staticmethod
    def __add_book_index_entry(book, description, doc):
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
    def __add_acquisiton_details(book, doc):
        entry = etree.SubElement(doc, "entry")
        etree.SubElement(entry, "title").text = book.Title

    def __add_acquisition_link(self, book, fileExt, doc):
        entry = doc.find("entry")
        booktype = self.__app.GetBookType(fileExt)

        e = etree.SubElement(entry, "link", attrib={
            "rel": "http://opds-spec.org/acquisition",
            "href": "/download/%s/%s" % (book.Id, fileExt),
            "type": booktype.MimeType})
        author = etree.SubElement(e, "author")
        etree.SubElement(author, "name").text = book.Author
        etree.SubElement(author, "uri").text = book.AuthorUri
