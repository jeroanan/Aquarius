import unittest
from aquarius.aquarius import aquarius
from aquarius.output.web.web import webserver
from aquarius.output.web.requesthandlers.requesthandler import requesthandler


class webserver_tests(unittest.TestCase):
    """Unit tests for the webserver class.
    Note: These were written after the code it tests."""

    def setUp(self):
        self.__a = AppMock()
        self.__r = RHSpy(self.__a)
        self.__w = webserver(self.__a, self.__r)
        self.__w.getUserAgent = lambda: "test"

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


class AppMock(aquarius):
    def __init__(self):
        super().__init__("hardcoded", None, None)

    def GetBookDetails(self, bookId):
        pass

    def GetBookType(self, formatcode):
        pass


class RHSpy(requesthandler):

    def __init__(self, app):
        super().__init__(app)
        self.indexhandlercalled = False
        self.bytitlecalled = False
        self.firstlettercalled = False
        self.bookcalled = False
        self.searchcalled = False
        self.harvestcalled = False

    def IndexHandler(self, useragent):
        self.indexhandlercalled = True

    def ByTitleHandler(self, useragent):
        self.bytitlecalled = True

    def FirstLetterHandler(self, useragent, first_letter):
        self.firstlettercalled = True

    def BookHandler(self, user_agent, bookId):
        self.bookcalled = True

    def Search(self, user_agent, search_term):
        self.searchcalled = True

    def HarvestHandler(self):
        self.harvestcalled = True