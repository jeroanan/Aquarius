from aquarius.output.web.requesthandlers.htmlrequesthandler import htmlrequesthandler


class HtmlRequestHandlerSpy(htmlrequesthandler):
    """A test stand-in for RequestHandler. Keeps track of what's been called
    for later reporting to unit tests."""
    def __init__(self):
        """Set initial object state"""
        super().__init__(None)
        self.index_handler_called = False
        self.first_letter_handler_called = False
        self.book_handler_called = False

    def SearchHandler(self, searchTerm):
        """Stand-in for search handler method"""
        return None

    def FirstLetterHandler(self, firstletter):
        """Stand-in for first letter handler method"""
        self.first_letter_handler_called = True
        return None

    def DownloadHandler(self, bookId, formatCode):
        """Stand-in for download handler method"""
        return None

    def BookHandler(self, bookId):
        """Stand-in for book handler method"""
        self.book_handler_called = True
        return None

    def IndexHandler(self):
        """Stand-in for index handler method"""
        self.index_handler_called = True
        return None

    def HarvestHandler(self):
        """Stand-in for harvest handler method"""
        return None

