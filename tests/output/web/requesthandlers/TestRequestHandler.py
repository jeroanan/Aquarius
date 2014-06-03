from aquarius.output.web.requesthandlers.RequestHandler import RequestHandler
from tests.output.web.requesthandlers.Mocks.HtmlRequestHandlerSpy import HtmlRequestHandlerSpy
from tests.output.web.requesthandlers.Mocks.OpdsRequestHandlerSpy import OpdsRequestHandlerSpy
from tests.output.web.requesthandlers.RequestHandlerTestBase import RequestHandlerTestBase


class TestRequestHandler(RequestHandlerTestBase):
    
    __webBrowserAgentString = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"
    __opdsAgentString = "Stanza iPhone/Aldiko/Moon+ Reader(Android)"
    
    def setUp(self):
        self.__html_spy = HtmlRequestHandlerSpy()
        self.__opds_spy = OpdsRequestHandlerSpy()
        RequestHandlerTestBase.initialise_app_mock(self)
        self.__r = RequestHandler(self.app)
        self.__r.set_html_request_handler(self.__html_spy)
        self.__r.set_opds_request_handler(self.__opds_spy)

    def test_requesting_index_with_a_web_browser_agent_calls_html_request_handler(self):
        self.__r.index_handler(self.__webBrowserAgentString)
        self.assertTrue(self.__html_spy.index_handler_called)

    def test_requesting_index_with_an_opds_agent_calls_opds_request_handler(self):
        self.__r.index_handler(self.__opdsAgentString)
        self.assertTrue(self.__opds_spy.index_handler_called)

    def test_requesting_by_title_with_an_opds_agent_calls_opds_request_handler(self):
        self.__r.by_title_handler(self.__opdsAgentString)
        self.assertTrue(self.__opds_spy.by_title_handler_called)

    def test_requesting_first_letter_with_an_opds_agent_calls_opds_request_handler(self):
        self.__r.first_letter_handler(self.__opdsAgentString, "t")
        self.assertTrue(self.__opds_spy.first_letter_handler_called)

    def test_requesting_first_letter_with_a_html_agent_calls_html_request_handler(self):
        self.__r.first_letter_handler(self.__webBrowserAgentString, "t")
        self.assertTrue(self.__html_spy.first_letter_handler_called)

    def test_requesting_book_with_an_opds_agent_calls_opds_request_handler(self):
        self.__r.book_handler(self.__opdsAgentString, "1")
        self.assertTrue(self.__opds_spy.book_handler_called)

    def test_requesting_book_with_a_html_agent_calls_html_request_handler(self):
        self.__r.book_handler(self.__webBrowserAgentString, "1")
        self.assertTrue(self.__html_spy.book_handler_called)

    def test_requesting_download_with_an_opds_agent_calls_opds_request_handler(self):
        self.__r.download_handler(self.__opdsAgentString, "1", "EPUB")
        self.assertTrue(self.__opds_spy.download_called)

    def test_requesting_search_with_an_opds_agent_calls_opds_request_handler(self):
        self.__r.search_handler(self.__opdsAgentString, "oo")
        self.assertTrue(self.__opds_spy.search_called)

    def test_requesting_search_with_a_web_browser_agent_calls_html_request_handler(self):
        self.__r.search_handler(self.__webBrowserAgentString, "oo")
        self.assertTrue(self.__html_spy.search_called)

    def test_requesting_harvest_with_a_web_browser_agent_calls_html_request_handler(self):
        self.__r.harvest_handler()
        self.assertTrue(self.__html_spy.harvest_called)
