from aquarius.output.web.requesthandlers.HtmlRequestHandler import HtmlRequestHandler


class HtmlRequestHandlerSpy(HtmlRequestHandler):
    """A test stand-in for RequestHandler. Keeps track of what's been called
    for later reporting to unit tests."""
    def __init__(self):
        """Set initial object state"""
        super().__init__(None)
        self.index_handler_called = False
        self.first_letter_handler_called = False
        self.book_handler_called = False
        self.search_called = False
        self.harvest_called = False

    def SearchHandler(self, search_term):
        """Stand-in for search handler method"""
        self.search_called = True
        return None

    def FirstLetterHandler(self, first_letter):
        """Stand-in for first letter handler method"""
        self.first_letter_handler_called = True
        return None

    def DownloadHandler(self, book_id, format_code):
        """Stand-in for download handler method"""
        return None

    def BookHandler(self, book_id):
        """Stand-in for book handler method"""
        self.book_handler_called = True
        return None

    def IndexHandler(self):
        """Stand-in for index handler method"""
        self.index_handler_called = True
        return None

    def HarvestHandler(self):
        """Stand-in for harvest handler method"""
        self.harvest_called = True
        return None

