import unittest

from aquarius.Aquarius import Aquarius
from aquarius.output.web.requesthandlers.RequestHandler import RequestHandler
from aquarius.output.web.requesthandlers.tests.Mocks.HtmlRequestHandlerSpy \
    import HtmlRequestHandlerSpy
from aquarius.output.web.requesthandlers.tests.Mocks.OpdsRequestHandlerSpy \
    import OpdsRequestHandlerSpy


class TestRequestHandler(unittest.TestCase):
    
    __webBrowserAgentString = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"
    __opdsAgentString = "Stanza iPhone/Aldiko/Moon+ Reader(Android)"
    
    def setUp(self):
        self.__html_spy = HtmlRequestHandlerSpy()
        self.__opds_spy = OpdsRequestHandlerSpy()
        self.__r = RequestHandler(Aquarius("hardcoded", None, None))
        self.__r.set_html_request_handler(self.__html_spy)
        self.__r.set_opds_request_handler(self.__opds_spy)

    def testRequestingIndexWithAWebBrowserAgentCallsHtmlRequestHandler(self):
        self.__r.index_handler(self.__webBrowserAgentString)
        self.assertTrue(self.__html_spy.index_handler_called)

    def testRequestingIndexWithAnOpdsAgentCallsOpdsRequestHandler(self):
        self.__r.index_handler(self.__opdsAgentString)
        self.assertTrue(self.__opds_spy.index_handler_called)

    def testRequestingByTitleWithAnOpdsAgentCallsOpdsRequestHandler(self):
        self.__r.by_title_handler(self.__opdsAgentString)
        self.assertTrue(self.__opds_spy.by_title_handler_called)

    def testRequestingFirstLetterWithAnOpdsAgentCallsOpdsRequestHandler(self):
        self.__r.first_letter_handler(self.__opdsAgentString, "t")
        self.assertTrue(self.__opds_spy.first_letter_handler_called)

    def testRequestingFirstLetterWithAHtmlAgentCallsHtmlRequestHandler(self):
        self.__r.first_letter_handler(self.__webBrowserAgentString, "t")
        self.assertTrue(self.__html_spy.first_letter_handler_called)

    def testRequestingBookWithAnOpdsAgentCallsOpdsRequestHandler(self):
        self.__r.book_handler(self.__opdsAgentString, "1")
        self.assertTrue(self.__opds_spy.book_handler_called)

    def testRequestingBookWithAHtmlAgentCallsHtmlRequestHandler(self):
        self.__r.book_handler(self.__webBrowserAgentString, "1")
        self.assertTrue(self.__html_spy.book_handler_called)

    def testRequestingDownloadWithAnOPDSAgentCallsOpdsRequestHandler(self):
        self.__r.download_handler(self.__opdsAgentString, "1", "EPUB")
        self.assertTrue(self.__opds_spy.download_called)

    def testRequestingSearchWithAnOpdsAgentCallsOpdsRequestHandler(self):
        self.__r.search_handler(self.__opdsAgentString, "oo")
        self.assertTrue(self.__opds_spy.search_called)

    def testRequestingSearchWithAWebBrowserAgentCallsHtmlRequestHandler(self):
        self.__r.search_handler(self.__webBrowserAgentString, "oo")
        self.assertTrue(self.__html_spy.search_called)

    def testRequestingHarvestWithAWebBrowserAgentCallsHtmlRequestHandler(self):
        self.__r.harvest_handler()
        self.assertTrue(self.__html_spy.harvest_called)
