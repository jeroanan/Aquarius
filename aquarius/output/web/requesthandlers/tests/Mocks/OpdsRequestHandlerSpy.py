import xml.etree.ElementTree as etree

from aquarius.output.web.requesthandlers.OpdsRequestHandler import OpdsRequestHandler


class OpdsRequestHandlerSpy(OpdsRequestHandler):
    def __init__(self):
        self.index_handler_called = False
        self.by_title_handler_called = False
        self.first_letter_handler_called = False
        self.book_handler_called = False
        self.download_called = False
        self.search_called = False
        super().__init__(None)

    def first_letter_handler(self, first_letter):
        self.first_letter_handler_called = True
        return etree.Element("moo")

    def by_title_handler(self):
        self.by_title_handler_called = True
        return etree.Element("moo")

    def download_handler(self, book_id, book_format):
        self.download_called = True
        return None

    def book_handler(self, book_id):
        self.book_handler_called = True
        return etree.Element("moo")

    def index_handler(self):
        self.index_handler_called = True
        return etree.Element("moo")

    def search_handler(self, search_term):
        self.search_called = True
        return etree.Element("moo")

