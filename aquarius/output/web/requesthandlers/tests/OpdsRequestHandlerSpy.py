import xml.etree.ElementTree as etree

from aquarius.output.web.requesthandlers.opdsrequesthandler import opdsrequesthandler


class OpdsRequestHandlerSpy(opdsrequesthandler):
    def __init__(self):
        self.index_handler_called = False
        self.by_title_handler_called = False
        self.first_letter_handler_called = False
        self.book_handler_called = False
        self.download_called = False
        self.search_called = False
        super().__init__(None)

    def FirstLetterHandler(self, firstletter):
        self.first_letter_handler_called = True
        return etree.Element("moo")

    def ByTitleHandler(self):
        self.by_title_handler_called = True
        return etree.Element("moo")

    def DownloadHandler(self, bookId, bookFormat):
        self.download_called = True
        return None

    def BookHandler(self, bookId):
        self.book_handler_called = True
        return etree.Element("moo")

    def IndexHandler(self):
        self.index_handler_called = True
        return etree.Element("moo")

    def Search(self, searchTerm):
        self.search_called = True
        return etree.Element("moo")

