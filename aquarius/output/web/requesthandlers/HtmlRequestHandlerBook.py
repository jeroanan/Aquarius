from jinja2 import Environment, PackageLoader


class HtmlRequestHandlerBook(object):

    def __init__(self, app):
        self.__app = app
        
    def handle(self, book_id):
        b = self.__app.get_book_details(book_id)
        env = Environment(loader=PackageLoader("aquarius", "output/web/html"))
        template = env.get_template("book.html")
        return template.render(book=b, page_title="%s - Aquarius EBook Library" % b.title)
    
    



