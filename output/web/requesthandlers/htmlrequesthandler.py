class htmlrequesthandler(object):
    
    def __init__(self, app):
        pass
    
    def IndexHandler(self):        
        with open("output/web/html/index.html", "r") as f:            
            return f.read()
    
    def SearchHandler(self, searchTerm):
        with open("output/web/html/search.html", "r") as f:            
            return f.read()
    
    
