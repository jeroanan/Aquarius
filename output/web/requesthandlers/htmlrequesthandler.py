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
        
    def BookHandler(self):
        return self.__getFileContents("output/web/html/book.html")
    
    def __getFileContents(self, fileName):
        with open(fileName, "r") as f:
            return f.read()
