from aquarius.output.web.requesthandlers.htmlrequesthandlersearch import htmlrequesthandlersearch
from aquarius.output.web.requesthandlers.htmlrequesthandlerbook import htmlrequesthandlerbook

class htmlrequesthandler(object):
    
    def __init__(self, app):
        self.__app = app
    
    def IndexHandler(self):
        return self.__getFileContents("aquarius/output/web/html/index.html")
    
    def SearchHandler(self, searchTerm):        
        return htmlrequesthandlersearch(self.__app).Handle(searchTerm)
        
    def HarvestHandler(self):
        self.__app.HarvestBooks()
        return self.IndexHandler()
        
    def BookHandler(self, bookId): 
        return htmlrequesthandlerbook(self.__app).Handle(bookId)
    
    def DownloadHandler(self, bookId, formatCode):
        book = self.__app.GetBookDetails(bookId)
        for thisFormat in book.Formats:
            if thisFormat.Format == formatCode:
                with open(thisFormat.Location, 'r') as f:
                    return f.read()
    
    def __getFileContents(self, fileName):
        with open(fileName, "r") as f:
            return f.read()   
