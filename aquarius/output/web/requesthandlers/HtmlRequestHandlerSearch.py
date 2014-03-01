from aquarius.output.web.requesthandlers.SearchTemplateHandler \
    import SearchTemplateHandler


class HtmlRequestHandlerSearch(object):
    """Handles html requests for book searches"""
    def __init__(self, app):
        """Set initial object state"""
        self.__app = app
        self.__search_template_handler = SearchTemplateHandler()

    def handle(self, search_term):
        """Handle the request"""
        r = list(self.__app.search_books(search_term))
        return self.__search_template_handler.render_search_template(r)

    def set_search_template_handler(self, handler):
        self.__search_template_handler = handler