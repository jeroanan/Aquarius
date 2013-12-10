from jinja2 import Environment, PackageLoader

class htmlrequesthandlersearch(object):
    
    def __init__(self, app):
        self.__app = app
        
    def Handle(self, searchTerm):        
        searchResults = self.__searchResultsToList(self.__app.SearchBooks(searchTerm))
        return self.__renderSearchTemplate("search.html", searchResults)
    
    def __searchResultsToList(self, results):
        out = []
        for r in results:
            out.append(r)
        return out
    
    def __renderSearchTemplate(self, templateFile, searchResults):
        env = Environment(loader=PackageLoader("aquarius", "output/web/html"))
        template = env.get_template(templateFile)
        return template.render(results=searchResults, totalbooks = len(searchResults))
    
    
        