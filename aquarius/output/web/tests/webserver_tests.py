import unittest
from aquarius.Aquarius import Aquarius
from aquarius.output.web.Web import WebServer
from aquarius.output.web.requesthandlers.RequestHandler import RequestHandler


class webserver_tests(unittest.TestCase):
    """Unit tests for the webserver class.
    Note: These were written after the code it tests."""

    def setUp(self):
        self.__a = AppMock()
        self.__r = RHSpy(self.__a)
        self.__w = WebServer(self.__a, self.__r)
        self.__w.get_user_agent = lambda: "test"

    def testIndexCallsRequestHandler(self):
        self.__w.index()
        self.assertTrue(self.__r.indexhandlercalled)

    def testByTitleCallsRequestHandler(self):
        self.__w.bytitle()
        self.assertTrue(self.__r.bytitlecalled)

    def testFirstLetterCallsRequestHandler(self):
        self.__w.firstletter("z")
        self.assertTrue(self.__r.firstlettercalled)

    def testBookCallsRequestHandler(self):
        self.__w.book(1)
        self.assertTrue(self.__r.bookcalled)

    def testSearchCallsRequestHandler(self):
        self.__w.search("search term")
        self.assertTrue(self.__r.searchcalled)

    def testHarvestCallsRequestHandler(self):
        self.__w.harvest()
        self.assertTrue(self.__r.harvestcalled)

    @staticmethod
    @unittest.skip
    def testDownloadDoesADownload():
        """At the moment I consider the download method untestable.
        It's been designed badly an has too much knowledge about books.
        It needs to just get a path back from the app and server it up
        without caring about what it is."""
        pass


class AppMock(Aquarius):
    def __init__(self):
        super().__init__("hardcoded", None, None)

    def GetBookDetails(self, bookId):
        pass

    def GetBookType(self, formatcode):
        pass


class RHSpy(RequestHandler):

    def __init__(self, app):
        super().__init__(app)
        self.indexhandlercalled = False
        self.bytitlecalled = False
        self.firstlettercalled = False
        self.bookcalled = False
        self.searchcalled = False
        self.harvestcalled = False

    def index_handler(self, useragent):
        self.indexhandlercalled = True

    def by_title_handler(self, useragent):
        self.bytitlecalled = True

    def first_letter_handler(self, useragent, first_letter):
        self.firstlettercalled = True

    def book_handler(self, user_agent, bookId):
        self.bookcalled = True

    def search_handler(self, user_agent, search_term):
        self.searchcalled = True

    def harvest_handler(self):
        self.harvestcalled = True