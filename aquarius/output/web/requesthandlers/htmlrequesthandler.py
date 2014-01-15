from aquarius.output.web.requesthandlers.htmlrequesthandlersearch import htmlrequesthandlersearch
from aquarius.output.web.requesthandlers.htmlrequesthandlerbook import htmlrequesthandlerbook
from aquarius.output.web.requesthandlers.htmlrequesthandlerfirstletter import htmlrequesthandlerfirstletter


class htmlrequesthandler(object):
    """Routes html requests to the relevant collaborator for fulfillment"""
    def __init__(self, app):
        """Set initial object state"""
        self.__app = app
        self.__search_handler = htmlrequesthandlersearch(self.__app)
        self.__book_handler = htmlrequesthandlerbook(self.__app)

    def IndexHandler(self):
        """Handle a request to the index page"""
        return self.__get_file_contents("aquarius/output/web/html/index.html")
    
    def SearchHandler(self, search_term):
        """Handle a request for a search"""
        return self.__search_handler.Handle(search_term)
        
    def HarvestHandler(self):
        """Handle a request to harvest books"""
        self.__app.HarvestBooks()
        return self.IndexHandler()
        
    def BookHandler(self, book_id):
        """Hanlde a request for book details"""
        return self.__book_handler.Handle(book_id)
    
    def DownloadHandler(self, book_id, format_code):
        """Handle a request to download a book"""
        book = self.__app.GetBookDetails(book_id)
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
        return htmlrequesthandlerfirstletter(self.__app).Handle(first_letter)

    def set_search_handler(self, handler):
        """Used by unit tests to set a test double for the search handler
        object. Not to be used in production."""
        self.__search_handler = handler

    def set_book_handler(self, handler):
        """Used by unit tests to set a test double for the book handler
        object. Not to be used in production."""
        self.__book_handler = handler