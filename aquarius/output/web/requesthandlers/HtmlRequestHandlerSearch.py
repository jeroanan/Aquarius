from aquarius.output.web.requesthandlers.SearchTemplateHandler \
    import SearchTemplateHandler


class HtmlRequestHandlerSearch(object):
    """Handles html requests for book searches"""
    def __init__(self, app):
        """Set initial object state"""
        self.__app = app
        
    def handle(self, search_term):
        """Handle the request"""
        r = list(self.__app.SearchBooks(search_term))
        return SearchTemplateHandler.render_search_template(r)
