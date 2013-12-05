from output.web.requesthandlers.requesthandler import requesthandler

import cherrypy
from cherrypy.lib.static import serve_file

class web(object):

    def __init__(self, app, config):
        self.__app = app
        self.__config = config
                
    def Main(self):
        cherrypy.config.update({
                                'server.socket_port': self.__config.WebServerPort, 
                                'server.socket_host': self.__config.WebServerAddress})
        cherrypy.tree.mount(webserver(self.__app), "", "output/web/app.config")
        cherrypy.engine.start()
        

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
    
    @cherrypy.expose
    def download(self, bookId, bookFormat):        
        book = self.__app.GetBookDetails(bookId)
        bookType = self.__app.GetBookType(bookFormat)        
        bookLocation = self.__getBookPath(bookFormat, book.Formats)
        print(bookLocation)
        return serve_file(bookLocation, bookType.MimeType, 'attachment')
    
    @cherrypy.expose
    def search(self, searchTerm):
        return requesthandler(self.__app).Search(self.__getUserAgent(), searchTerm)
        
    def __getBookPath(self, bookFormat, bookFormats):
        for theFormat in bookFormats:
            if theFormat.Format == bookFormat:
                return theFormat.Location
            
    def __getUserAgent(self):
        return cherrypy.request.headers["User-Agent"]
    


