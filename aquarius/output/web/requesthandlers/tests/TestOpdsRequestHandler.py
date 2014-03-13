import xml.etree.ElementTree as etree

from unittest.mock import Mock
from aquarius.Aquarius import Aquarius
from aquarius.objects.Book import Book
from aquarius.objects.bookformat import bookformat
from aquarius.objects.booktype import booktype
from aquarius.output.web.requesthandlers.Jinja2Loader import Jinja2Loader
from aquarius.output.web.requesthandlers.OpdsRequestHandler import OpdsRequestHandler

import unittest


class TestOpdsRequestHandler(unittest.TestCase):

    def setUp(self):
        self.__setup_app_mock()
        self.__loader = Jinja2Loader()
        self.__loader.load_template = Mock()
        self.__opds_request_handler = OpdsRequestHandler(self.__app, self.__loader)

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

    def test_index_handler_calls_template_loader(self):
        self.__opds_request_handler.index_handler()
        self.assertTrue(self.__loader.load_template.called)

    def test_by_title_handler_gives_the_correct_feed_header(self):
        self.__check_common_header(self.__opds_request_handler.by_title_handler(), "Browse books by title")
        
    def test_by_title_handler_contains_the_correct_number_of_entries(self):
        x = self.__opds_request_handler.by_title_handler()
        self.assertEqual(36, len(x.findall("entry")))
        
    def test_first_letter_handler_gives_the_correct_feed_header(self):
        self.__opds_request_handler.first_letter_handler("")
        self.assertTrue(self.__app.list_books_by_first_letter.called)
        self.assertTrue(self.__loader.load_template.called)

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
