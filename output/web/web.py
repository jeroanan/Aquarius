import cherrypy

class web(object):

    def __init__(self, app, config):
        self.__app = app
        self.__config = config
                
    def Main(self):
        cherrypy.config.update({'server.socket_port': 8080, 'server.socket_host:': 'localhost'})
        cherrypy.quickstart(webserver(self.__app))
        

class webserver(object):
    
    def __init__(self, app):
        self.__app = app
        
    @cherrypy.expose
    def index(self):
        with open('output/web/html/index.html', 'r') as f:
            return f.read()
    


