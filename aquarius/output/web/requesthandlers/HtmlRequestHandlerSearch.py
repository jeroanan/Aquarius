from aquarius.output.web.requesthandlers.SearchTemplateHandler \
    import SearchTemplateHandler


class HtmlRequestHandlerSearch(object):

    def __init__(self, app):
        self.__app = app
        self.__search_template_handler = SearchTemplateHandler()

    def handle(self, search_term):
        r = list(self.__app.search_books(search_term))
        return self.__search_template_handler.render_search_template(r, self.__app)

    def set_search_template_handler(self, handler):
        self.__search_template_handler = handler