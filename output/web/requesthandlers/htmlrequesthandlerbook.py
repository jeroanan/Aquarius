from jinja2 import Environment, PackageLoader

class htmlrequesthandlerbook(object):   
    
    def __init__(self, app):
        self.__app = app
        
    def Handle(self, bookId):
        b  = self.__app.GetBookDetails(bookId)        
        env = Environment(loader=PackageLoader("aquarius", "output/web/html"))
        template = env.get_template("book.html")
        return template.render(book=b)
    
    



