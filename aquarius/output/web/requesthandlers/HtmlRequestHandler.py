from aquarius.output.web.requesthandlers.HtmlRequestHandlerDownload import HtmlRequestHandlerDownload
from aquarius.output.web.requesthandlers.HtmlRequestHandlerIndex import HtmlRequestHandlerIndex
from aquarius.output.web.requesthandlers.HtmlRequestHandlerSearch \
    import HtmlRequestHandlerSearch
from aquarius.output.web.requesthandlers.HtmlRequestHandlerBook \
    import HtmlRequestHandlerBook
from aquarius.output.web.requesthandlers.HtmlRequestHandlerFirstLetter \
    import HtmlRequestHandlerFirstLetter


class HtmlRequestHandler(object):

    def __init__(self, app):
        self.__app = app
        self.__search_handler = HtmlRequestHandlerSearch(self.__app)
        self.__book_handler = HtmlRequestHandlerBook(self.__app)
        self.__first_letter_handler = HtmlRequestHandlerFirstLetter(self.__app)
        self.__index_handler = HtmlRequestHandlerIndex(self.__app)
        self.__download_handler = HtmlRequestHandlerDownload(self.__app)

    def index_handler(self):
        return self.__index_handler.handle()
    
    def search_handler(self, search_term):
        return self.__search_handler.handle(search_term)
        
    def harvest_handler(self):
        self.__app.harvest_books()
        return self.index_handler()
        
    def book_handler(self, book_id):
        return self.__book_handler.handle(book_id)
    
    def download_handler(self, book_id, format_code):
        self.__download_handler.handle(book_id, format_code)
    
    def first_letter_handler(self, first_letter):
        return self.__first_letter_handler.handle(first_letter)

    def set_search_handler(self, handler):
        self.__search_handler = handler

    def set_book_handler(self, handler):
        self.__book_handler = handler

    def set_first_letter_handler(self, handler):
        self.__first_letter_handler = handler

    def set_index_handler(self, handler):
        self.__index_handler = handler

    def set_download_handler(self, download_handler):
        self.__download_handler = download_handler