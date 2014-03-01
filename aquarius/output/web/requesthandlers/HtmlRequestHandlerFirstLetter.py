from aquarius.output.web.requesthandlers.SearchTemplateHandler \
    import SearchTemplateHandler


class HtmlRequestHandlerFirstLetter(object):

    def __init__(self, app):
        self.__app = app
        self.__search_template_handler = SearchTemplateHandler()

    def handle(self, first_letter):
        r = list(self.__app.list_books_by_first_letter(first_letter))
        return self.__search_template_handler.render_search_template(r)

    def set_search_template_handler(self, handler):
        self.__search_template_handler = handler