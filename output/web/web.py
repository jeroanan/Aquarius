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
        return requesthandler(self.__app).IndexHandler(self.__getUserAgent())
    
    @cherrypy.expose
    def bytitle(self):
        return requesthandler(self.__app).ByTitleHandler(self.__getUserAgent())
     
    @cherrypy.expose
    def firstletter(self, letter):
        return requesthandler(self.__app).FirstLetterHandler(self.__getUserAgent(), letter)    

    @cherrypy.expose
    def book(self, bookId):
        return requesthandler(self.__app).BookHandler(self.__getUserAgent(), bookId)
    
    def __getUserAgent(self):
        return cherrypy.request.headers["User-Agent"]
    


