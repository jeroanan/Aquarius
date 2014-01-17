from jinja2 import Environment, PackageLoader


class HtmlRequestHandlerBook(object):
    """Handles html requests for the details of a specific book"""
    def __init__(self, app):
        """Set initial object state"""
        self.__app = app
        
    def handle(self, book_id):
        """Handle the request"""
        b = self.__app.get_book_details(book_id)
        env = Environment(loader=PackageLoader("aquarius", "output/web/html"))
        template = env.get_template("book.html")
        return template.render(book=b)
    
    



