import xml.etree.ElementTree as etree

from unittest.mock import Mock
from aquarius.Aquarius import Aquarius
from aquarius.objects.Book import Book
from aquarius.objects.bookformat import bookformat
from aquarius.objects.booktype import booktype
from aquarius.output.web.requesthandlers.OpdsRequestHandler import OpdsRequestHandler

import unittest


class TestOpdsRequestHandler(unittest.TestCase):

    def setUp(self):
        self.__setup_app_mock()
        self.__opds_request_handler = OpdsRequestHandler(self.__app, None)

        with open("./1.EPUB", 'w') as f:
            f.write("test\n")

    def __setup_app_mock(self):
        b = self.__get_mock_book()
        self.__app = Aquarius("hardcoded", None, None)
        self.__app.search_books = Mock(return_value=[Book()])
        self.__app.get_book_details = Mock(return_value=b)
        self.__app.get_book_type = Mock()
        self.__app.list_books_by_first_letter = Mock(return_value=[])

    def __get_mock_book(self):
        b = Book()
        b.id = 1414
        b.title = "Title"
        b.author = "An Author"
        b.author_uri = "about:none"
        f = bookformat()
        b.formats = [f, f, f]
        return b
        
    def __check_common_header(self, xml_doc, expected_title):
        self.assertEqual("feed", xml_doc.tag)
        self.assertEqual("http://www.w3.org/2005/Atom",
                         xml_doc.attrib["xmlns"])
        self.assertEqual("http://opds-spec.org/2010/catalog",
                         xml_doc.attrib["xmlns:opds"])
        self.assertEqual(len(xml_doc.findall('id')), 1)
        self.assertEqual(len(xml_doc.findall('title')), 1)
        self.assertEqual(xml_doc.findall('title')[0].text, expected_title)
        self.assertEqual(len(xml_doc.findall('link')), 1)
    
    def test_index_handler_gives_the_correct_feed_header(self):
        self.__check_common_header(self.__opds_request_handler.index_handler(), "Aquarius EBook library")
    
    def test_index_handler_feed_tag_contains_the_correct_links(self):
        xml = self.__opds_request_handler.index_handler()
        link_element = xml.findall('link')[0]
        self.assertEqual("/search/{searchTerms}", link_element.attrib['href'])
        self.assertEqual("application/atom+xml", link_element.attrib["type"])
        self.assertEqual("search", link_element.attrib["rel"])
        self.assertEqual("Search", link_element.attrib["title"])
        
    def test_index_handler_contains_some_entries(self):
        x = self.__opds_request_handler.index_handler()
        self.assertGreater(len(x.findall('entry')), 0)
        
    def test_index_handler_first_entry_title_is_browse_by_title(self):
        x = self.__opds_request_handler.index_handler().findall('entry')[0]
        self.assertEqual(len(x.findall('title')), 1)
        self.assertEqual(x.findall('title')[0].text, "List By Letter")
        
    def test_index_handler_first_entry_link_is_correct(self):
        x = self.__opds_request_handler.index_handler().findall('entry')[0]
        self.assertEqual(len(x.findall('link')), 1)
        link_element = x.findall("link")[0]
        self.assertEqual(link_element.attrib["rel"], "subsection")
        self.assertEqual(link_element.attrib["href"], "/bytitle")
        t = "application/atom+xml;profile=opds-catalog;kind=acquisition"
        self.assertEqual(link_element.attrib["type"], t)

    def test_index_handler_first_entry_is_correct(self):
        x = self.__opds_request_handler.index_handler().findall('entry')[0]
        self.assertEqual(len(x.findall("id")), 1)
        self.assertEqual(len(x.findall("content")), 1)
        content_element = x.findall("content")[0]
        self.assertEqual(content_element.attrib["content"], "text")
        self.assertEqual("Browse books by title", content_element.text)

    def test_by_title_handler_gives_the_correct_feed_header(self):
        self.__check_common_header(self.__opds_request_handler.by_title_handler(), "Browse books by title")
        
    def test_by_title_handler_contains_the_correct_number_of_entries(self):
        x = self.__opds_request_handler.by_title_handler()
        self.assertEqual(36, len(x.findall("entry")))
        
    def test_first_letter_handler_gives_the_correct_feed_header(self):
        self.__opds_request_handler.first_letter_handler("")

    def test_book_handler_gives_the_correct_feed_header(self):
        self.__check_common_header(self.__opds_request_handler.book_handler("1"), "Aquarius EBook Library")

    def test_book_has_the_correct_acquisition_links(self):
        x = self.__opds_request_handler.book_handler("1")
        self.assertEqual(3, len(x.findall("entry/link")))
    
    def test_book_handler_gives_the_correct_author(self):
        bt = booktype()
        bt.Format="EPUB"
        bt.MimeType="MIME"
        self.__app.get_book_type = Mock(return_value=bt)
        x = self.__opds_request_handler.book_handler("1")
        print(etree.tostring(x))
        self.assertEqual("An Author", x.findall("entry/link/author/name")[0].text)
        self.assertEqual("about:none", x.findall("entry/link/author/uri")[0].text)

    @unittest.skip("This method isn't testable at the moment")
    def test_download_gets_book(self):
        x = self.__opds_request_handler.download_handler("1", "EPUB")
        self.assertNotEqual(None, x)        
        
    def test_search_gives_the_correct_feed_header(self):
        x = self.__opds_request_handler.search_handler("oo")
        self.__check_common_header(x, "Search results for oo")
    
    def test_search_returns_no_book_when_the_search_query_has_no_results(self):
        self.__app.search_books = Mock(return_value=[])
        x = self.__opds_request_handler.search_handler("sdkljsadjaskl")
        self.assertEqual(0, len(x.findall("entry")))
        
    def test_search_returns_a_book_when_the_search_query_has_a_result(self):
        x = self.__opds_request_handler.search_handler("oo")
        self.assertEqual(1, len(x.findall("entry")))
