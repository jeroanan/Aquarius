class htmlrequesthandler(object):
    
    def IndexHandler(self):        
        with open("output/web/html/index.html", "r") as f:            
            return f.read()
    
    def SearchHandler(self):
        print("moo")
        with open("output/web/html/search.html", "r") as f:            
            return f.read()
    
    
