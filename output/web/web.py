import cherrypy

class web(object):

    def __init__(self, app, config):
        self.__app = app
        self.__config = config
                
    def Main(self):
        cherrypy.config.update({
                                'server.socket_port': self.__config.WebServerPort, 
                                'server.socket_host': self.__config.WebServerAddress})
        cherrypy.quickstart(webserver(self.__app))
        

class webserver(object):
    
    def __init__(self, app):
        self.__app = app
        
    @cherrypy.expose
    def index(self):
        if not self.__IsOpdsBrowser():        
            with open('output/web/html/index.html', 'r') as f:
                return f.read()
    
    def __IsOpdsBrowser(self):
        #Stanza iPhone/Aldiko/Moon+ Reader(Android)t.app)
        return cherrypy.request.headers["User-Agent"].find("Aldiko")>-1


