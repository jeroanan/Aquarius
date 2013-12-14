from jinja2 import Environment, PackageLoader

from output.web.requesthandlers.htmlrequesthandlersearch import htmlrequesthandlersearch

class htmlrequesthandler(object):
    
    def __init__(self, app):
        self.__app = app
    
    def IndexHandler(self):
        return self.__getFileContents("output/web/html/index.html")
    
    def SearchHandler(self, searchTerm):        
        return htmlrequesthandlersearch(self.__app).Handle(searchTerm)
        
    def HarvestHandler(self):
        self.__app.HarvestBooks()
        return self.IndexHandler()
        
    def BookHandler(self, bookId):        
        b  = self.__app.GetBookDetails(bookId)
        env = Environment(loader=PackageLoader("aquarius", "output/web/html"))
        template = env.get_template("book.html")
        return template.render(book=b)
    
    def __getFileContents(self, fileName):
        with open(fileName, "r") as f:
            return f.read()
