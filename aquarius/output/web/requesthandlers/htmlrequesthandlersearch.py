from jinja2 import Environment, PackageLoader

class htmlrequesthandlersearch(object):
    
    def __init__(self, app):
        self.__app = app
        
    def Handle(self, searchTerm):        
        searchResults = list(self.__app.SearchBooks(searchTerm))
        return self.__renderSearchTemplate("search.html", searchResults)
        
    def __renderSearchTemplate(self, templateFile, searchResults):
        env = Environment(loader=PackageLoader("aquarius", "output/web/html"))
        template = env.get_template(templateFile)
        return template.render(results=searchResults, totalbooks = len(searchResults))
    
    
        