from output.web.requesthandlers.requesthandler import requesthandler

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
        return requesthandler().IndexHandler(self.__getUserAgent())
    
    @cherrypy.expose
    def bytitle(self):
        return requesthandler().ByTitleHandler(self.__getUserAgent())
     
    def __getUserAgent(self):
        return cherrypy.request.headers["User-Agent"]
    


