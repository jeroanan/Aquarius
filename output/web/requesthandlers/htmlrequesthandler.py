class htmlrequesthandler(object):
    
    def IndexHandler(self):        
        with open("output/web/html/index.html", "r") as f:            
            return f.read()