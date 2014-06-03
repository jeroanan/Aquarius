from unittest.mock import Mock

from aquarius.objects.Book import Book
from aquarius.objects.BookFormat import BookFormat
from aquarius.output.web.requesthandlers.Jinja2Loader import Jinja2Loader
from aquarius.output.web.requesthandlers.OpdsRequestHandler import OpdsRequestHandler
from tests.output.web.requesthandlers.RequestHandlerTestBase import RequestHandlerTestBase


class TestOpdsRequestHandler(RequestHandlerTestBase):

    def setUp(self):
        self.__initialise_app_mock()
        self.__loader = Jinja2Loader()
        self.__loader.load_template = Mock()
        self.__opds_request_handler = OpdsRequestHandler(self.app, self.__loader)

    def __initialise_app_mock(self):
        RequestHandlerTestBase.initialise_app_mock(self)
        b = self.__get_mock_book()
        self.app.search_books = Mock()
        self.app.get_book_details = Mock(return_value=b)
        self.app.get_book_type = Mock()
        self.app.list_books_by_first_letter = Mock()

    def __get_mock_book(self):
        b = Book()
        b.id = 1414
        b.title = "Title"
        b.author = "An Author"
        b.author_uri = "about:none"
        f = BookFormat()
        b.formats = [f, f, f]
        return b
        
    def test_index_handler_calls_template_loader(self):
        self.__opds_request_handler.index_handler()
        self.assert_called(self.__loader.load_template)

    def test_by_title_handler_calls_template_loader(self):
        self.__opds_request_handler.by_title_handler()
        self.assert_called(self.__loader.load_template)

    def test_first_letter_handler_gives_the_correct_feed_header(self):
        self.__opds_request_handler.first_letter_handler("")
        self.assert_called(self.app.list_books_by_first_letter)
        self.assert_called(self.__loader.load_template)

    def test_book_handler_calls_template_loader(self):
        self.__opds_request_handler.book_handler("1")
        self.assert_called(self.__loader.load_template)

    def test_search_calls_template_loader(self):
        self.__opds_request_handler.search_handler("oo")
        self.assert_called(self.app.search_books)
        self.assert_called(self.__loader.load_template)