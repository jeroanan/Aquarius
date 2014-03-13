from unittest.mock import Mock
import unittest

from aquarius.Aquarius import Aquarius
from aquarius.objects.Book import Book
from aquarius.objects.bookformat import bookformat
from aquarius.output.web.requesthandlers.Jinja2Loader import Jinja2Loader
from aquarius.output.web.requesthandlers.OpdsRequestHandler import OpdsRequestHandler


class TestOpdsRequestHandler(unittest.TestCase):

    def setUp(self):
        self.__setup_app_mock()
        self.__loader = Jinja2Loader()
        self.__loader.load_template = Mock()
        self.__opds_request_handler = OpdsRequestHandler(self.__app, self.__loader)

    def __setup_app_mock(self):
        b = self.__get_mock_book()
        self.__app = Aquarius("hardcoded", None, None)
        self.__app.search_books = Mock()
        self.__app.get_book_details = Mock(return_value=b)
        self.__app.get_book_type = Mock()
        self.__app.list_books_by_first_letter = Mock()

    def __get_mock_book(self):
        b = Book()
        b.id = 1414
        b.title = "Title"
        b.author = "An Author"
        b.author_uri = "about:none"
        f = bookformat()
        b.formats = [f, f, f]
        return b
        
    def test_index_handler_calls_template_loader(self):
        self.__opds_request_handler.index_handler()
        self.assertTrue(self.__loader.load_template.called)

    def test_by_title_handler_calls_template_loader(self):
        self.__opds_request_handler.by_title_handler()
        self.assertTrue(self.__loader.load_template.called)

    def test_first_letter_handler_gives_the_correct_feed_header(self):
        self.__opds_request_handler.first_letter_handler("")
        self.assertTrue(self.__app.list_books_by_first_letter.called)
        self.assertTrue(self.__loader.load_template.called)

    def test_book_handler_calls_template_loader(self):
        self.__opds_request_handler.book_handler("1")
        self.assertTrue(self.__loader.load_template.called)

    @unittest.skip("This method isn't testable at the moment")
    def test_download_gets_book(self):
        x = self.__opds_request_handler.download_handler("1", "EPUB")
        self.assertNotEqual(None, x)        
        
    def test_search_calls_template_loader(self):
        self.__opds_request_handler.search_handler("oo")
        self.assertTrue(self.__app.search_books.called)
        self.assertTrue(self.__loader.load_template.called)