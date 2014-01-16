from aquarius.output.web.requesthandlers.SearchTemplateHandler \
    import SearchTemplateHandler


class HtmlRequestHandlerFirstLetter(object):
    """Handles html requests to list all books beginning with a given letter"""
    def __init__(self, app):
        """Set initial object state"""
        self.__app = app

    def handle(self, firstletter):
        """Handle the request"""
        r = list(self.__app.ListBooksByFirstLetter(firstletter))
        return SearchTemplateHandler.render_search_template(r)
