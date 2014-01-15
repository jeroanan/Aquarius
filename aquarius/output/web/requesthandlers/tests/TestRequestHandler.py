import unittest

from aquarius.aquarius import aquarius
from aquarius.output.web.requesthandlers.requesthandler import requesthandler
from aquarius.output.web.requesthandlers.tests.Mocks.HtmlRequestHandlerSpy \
    import HtmlRequestHandlerSpy
from aquarius.output.web.requesthandlers.tests.Mocks.OpdsRequestHandlerSpy \
    import OpdsRequestHandlerSpy


class TestRequestHandler(unittest.TestCase):
    
    __webBrowserAgentString = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"
    __opdsAgentString = "Stanza iPhone/Aldiko/Moon+ Reader(Android)"
    
    def setUp(self):
        """Common setup operations"""
        self.__html_spy = HtmlRequestHandlerSpy()
        self.__opds_spy = OpdsRequestHandlerSpy()
        self.__r = requesthandler(aquarius("hardcoded", None, None))
        self.__r.set_html_request_handler(self.__html_spy)
        self.__r.set_opds_request_handler(self.__opds_spy)

    def testRequestingIndexWithAWebBrowserAgentCallsHtmlRequestHandler(self):
        """Given an index request, when it's done with a web browser agent
        string, then tell the html request handler to fulfill the request"""
        self.__r.IndexHandler(self.__webBrowserAgentString)
        self.assertTrue(self.__html_spy.index_handler_called)

    def testRequestingIndexWithAnOpdsAgentCallsOpdsRequestHandler(self):
        """Given an index request, when it's done with an opds browser agent
        string, then tell the opds request handler to fulfill the request."""
        self.__r.IndexHandler(self.__opdsAgentString)
        self.assertTrue(self.__opds_spy.index_handler_called)

    def testRequestingByTitleWithAnOpdsAgentCallsOpdsRequestHandler(self):
        """Given a by title request, when it's done with an opds browser agent
        string, then tell the opds request handler to fulfill the request"""
        self.__r.ByTitleHandler(self.__opdsAgentString)
        self.assertTrue(self.__opds_spy.by_title_handler_called)

    def testRequestingFirstLetterWithAnOpdsAgentCallsOpdsRequestHandler(self):
        """Given a first letter request, when it's done with an opds browser
        agent, then tell the opds request handler to fulfill the request"""
        self.__r.FirstLetterHandler(self.__opdsAgentString, "t")
        self.assertTrue(self.__opds_spy.first_letter_handler_called)

    def testRequestingFirstLetterWithAHtmlAgentCallsHtmlRequestHandler(self):
        """Given a first letter request, when it's done with an html browser
        agent, then tell the html request handler to fulfill the request"""
        self.__r.FirstLetterHandler(self.__webBrowserAgentString, "t")
        self.assertTrue(self.__html_spy.first_letter_handler_called)

    def testRequestingBookWithAnOpdsAgentCallsOpdsRequestHandler(self):
        """Given a book request, when it's done with an opds browser agent,
        then tell the opds request handler to fulfill the request"""
        self.__r.BookHandler(self.__opdsAgentString, "1")
        self.assertTrue(self.__opds_spy.book_handler_called)

    def testRequestingBookWithAHtmlAgentCallsHtmlRequestHandler(self):
        """Given a book request, when it's done with an html browser agent,
        then tell the html request handler to fulfill the request"""
        self.__r.BookHandler(self.__webBrowserAgentString, "1")
        self.assertTrue(self.__html_spy.book_handler_called)

    def testRequestingDownloadWithAnOPDSAgentCallsOpdsRequestHandler(self):
        """Given a download request, when it's done with an opds browser agent,
        then tell the opds request handler to fulfill the request"""
        self.__r.DownloadHandler(self.__opdsAgentString, "1", "EPUB")
        self.assertTrue(self.__opds_spy.download_called)

    def testRequestingSearchWithAnOpdsAgentCallsOpdsRequestHandler(self):
        """Given a search request, when it's done with an opds browser agent,
        then tell the opds request handler to fulfill the request"""
        self.__r.Search(self.__opdsAgentString, "oo")
        self.assertTrue(self.__opds_spy.search_called)

    def testRequestingSearchWithAWebBrowserAgentCallsHtmlRequestHandler(self):
        """Given a search request, when it's done with an html browser agent,
        then tell the html request handler to fulfill the request"""
        self.__r.Search(self.__webBrowserAgentString, "oo")
        self.assertTrue(self.__html_spy.search_called)

    def testRequestingHarvestWithAWebBrowserAgentCallsHtmlRequestHandler(self):
        """Given a harvest request, when it's done with an html browser agent,
        then tell the html request handler to fulfill the request"""
        self.__r.HarvestHandler()
        self.assertTrue(self.__html_spy.harvest_called)
