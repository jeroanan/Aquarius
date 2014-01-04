from aquarius.output.web.requesthandlers.searchtemplatehelper import searchtemplatehelper

class htmlrequesthandlersearch(object):
    
    def __init__(self, app):
        self.__app = app
        
    def Handle(self, searchTerm):        
        searchResults = list(self.__app.SearchBooks(searchTerm))
        return searchtemplatehelper.RenderSearchTemplate(searchResults)        
    
    
    
        