from jinja2 import Environment, PackageLoader

class htmlrequesthandler(object):
    
    def __init__(self, app):
        self.__app = app
    
    def IndexHandler(self):        
        with open("output/web/html/index.html", "r") as f:            
            return f.read()
    
    def SearchHandler(self, searchTerm):        
        searchResults = self.__app.SearchBooks(searchTerm)
        return self.__renderSearchTemplate("search.html", searchResults)
    
    def __renderSearchTemplate(self, templateFile, searchResults):
        env = Environment(loader=PackageLoader("aquarius", "output/web/html"))
        template = env.get_template(templateFile)
        return template.render(results=searchResults)
    
