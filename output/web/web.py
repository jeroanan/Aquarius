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
        self.__requesthandler = requesthandler(app)
        
    @cherrypy.expose
    def index(self):
        return self.__requesthandler.IndexHandler(self.__getUserAgent())
    
    @cherrypy.expose
    def bytitle(self):
        return self.__requesthandler.ByTitleHandler(self.__getUserAgent())
     
    @cherrypy.expose
    def firstletter(self, letter):
        return self.__requesthandler.FirstLetterHandler(self.__getUserAgent(), letter)    

    @cherrypy.expose
    def book(self, bookId):
        return self.__requesthandler.BookHandler(self.__getUserAgent(), bookId)
    
    @cherrypy.expose
    def download(self, bookId, bookFormat):        
        book = self.__app.GetBookDetails(bookId)
        bookType = self.__app.GetBookType(bookFormat)        
        bookLocation = self.__getBookPath(bookFormat, book.Formats)
        return serve_file(bookLocation, bookType.MimeType, 'attachment')
    
    @cherrypy.expose
    def search(self, searchTerm):
        return self.__requesthandler.Search(self.__getUserAgent(), searchTerm)
    
    @cherrypy.expose    
    def harvest(self):
        return self.__requesthandler.HarvestHandler()
    
    def __getBookPath(self, bookFormat, bookFormats):
        for theFormat in bookFormats:
            if theFormat.Format == bookFormat:
                return theFormat.Location
            
    def __getUserAgent(self):
        return cherrypy.request.headers["User-Agent"]
    