class HtmlRequestHandlerDelegateSpy(object):
    """Test double for the HtmlRequestHandlerSearch class"""
    def __init__(self):
        """Set superclass initial state"""
        self.handle_called = False

    def Handle(self, search_term):
        """Simulate the Handler method"""
        self.handle_called = True
        return None


