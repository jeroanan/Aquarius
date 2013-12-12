from output.web.requesthandlers.htmlrequesthandlersearch import htmlrequesthandlersearch

class htmlrequesthandler(object):
    
    def __init__(self, app):
        self.__app = app
    
    def IndexHandler(self):        
        with open("output/web/html/index.html", "r") as f:            
            return f.read()
    
    def SearchHandler(self, searchTerm):        
        return htmlrequesthandlersearch(self.__app).Handle(searchTerm)
        
    def HarvestHandler(self):
        self.__app.HarvestBooks()
        return self.IndexHandler()
