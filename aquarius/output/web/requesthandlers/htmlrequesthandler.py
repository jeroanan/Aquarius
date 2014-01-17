from aquarius.output.web.requesthandlers.HtmlRequestHandlerSearch import HtmlRequestHandlerSearch
from aquarius.output.web.requesthandlers.HtmlRequestHandlerBook import HtmlRequestHandlerBook
from aquarius.output.web.requesthandlers.HtmlRequestHandlerFirstLetter import HtmlRequestHandlerFirstLetter


class htmlrequesthandler(object):
    """Routes html requests to the relevant collaborator for fulfillment"""
    def __init__(self, app):
        """Set initial object state"""
        self.__app = app
        self.__search_handler = HtmlRequestHandlerSearch(self.__app)
        self.__book_handler = HtmlRequestHandlerBook(self.__app)
        self.__first_letter_handler = HtmlRequestHandlerFirstLetter(self.__app)

    def IndexHandler(self):
        """Handle a request to the index page"""
        return self.__get_file_contents("aquarius/output/web/html/index.html")
    
    def SearchHandler(self, search_term):
        """Handle a request for a search"""
        return self.__search_handler.handle(search_term)
        
    def HarvestHandler(self):
        """Handle a request to harvest books"""
        self.__app.HarvestBooks()
        return self.IndexHandler()
        
    def BookHandler(self, book_id):
        """Hanlde a request for book details"""
        return self.__book_handler.handle(book_id)
    
    def DownloadHandler(self, book_id, format_code):
        """Handle a request to download a book"""
        book = self.__app.get_book_details(book_id)
        for thisFormat in book.Formats:
            if thisFormat.Format == format_code:
                with open(thisFormat.Location, 'r') as f:
                    return f.read()
    
    @staticmethod
    def __get_file_contents(file_name):
        with open(file_name, "r") as f:
            return f.read()   
    
    def FirstLetterHandler(self, first_letter):
        """Handle a request to list books by first letter"""
        return self.__first_letter_handler.handle(first_letter)

    def set_search_handler(self, handler):
        """Used by unit tests to set a test double for the search handler
        object. Not to be used in production."""
        self.__search_handler = handler

    def set_book_handler(self, handler):
        """Used by unit tests to set a test double for the book handler
        object. Not to be used in production."""
        self.__book_handler = handler

    def set_first_letter_handler(self, handler):
        """Used by unit tests to set a test double for the first letter handler
        object. Not to be used in production."""
        self.__first_letter_handler = handler