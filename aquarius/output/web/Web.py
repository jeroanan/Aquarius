import cherrypy
from cherrypy.lib.static import serve_file


class Web(object):
    """Begins and holds the cherrypy instance"""
    def __init__(self, app, config):
        """Set up initial object state"""
        self.__app = app
        self.__config = config
                
    def main(self):
        """Start up cherrypy"""
        cherrypy.config.update({
            'server.socket_port': self.__config.web_server_port,
            'server.socket_host': self.__config.web_server_address})
        cherrypy.tree.mount(WebServer(self.__app), "", "aquarius/output/web/app.config")
        cherrypy.engine.start()        


class WebServer(object):
    """Functions that are called by cherrypy when a http request is made"""
    def __init__(self, app, request_handler):
        """Set initial object state"""
        self.__app = app
        self.request_handler = request_handler

    #TODO: A lot of these names are not PEP8-compliant because to make them
    # so would break the web addresses Aquarius uses. Look up cherrypy
    # configuration so we can have urls that are different from
    # function names.
    @cherrypy.expose
    def index(self):
        """Index page handler"""
        return self.request_handler.index_handler(self.get_user_agent())
    
    @cherrypy.expose
    def bytitle(self):
        """bytitle page handler"""
        return self.request_handler.by_title_handler(self.get_user_agent())
     
    @cherrypy.expose
    def firstletter(self, letter):
        """firstletter page handler"""
        return self.request_handler.first_letter_handler(self.get_user_agent(), letter)

    @cherrypy.expose
    def book(self, bookId):
        """book page handler"""
        return self.request_handler.book_handler(self.get_user_agent(), bookId)
    
    @cherrypy.expose
    def download(self, bookId, bookFormat):
        """Bookd download handler"""
        book = self.__app.GetBookDetails(bookId)
        bookType = self.__app.GetBookType(bookFormat)        
        bookLocation = self.__get_book_path(bookFormat, book.Formats)
        return serve_file(bookLocation, bookType.MimeType, 'attachment')
    
    @cherrypy.expose
    def search(self, searchTerm):
        """Search page handler"""
        return self.request_handler.search_handler(self.get_user_agent(), searchTerm)
    
    @cherrypy.expose    
    def harvest(self):
        """Book harvest handler"""
        return self.request_handler.harvest_handler()
    
    @staticmethod
    def __get_book_path(book_format, book_formats):
        for theFormat in book_formats:
            if theFormat.Format == book_format:
                return theFormat.Location
            
    @staticmethod
    def get_user_agent():
        """Gets the requesting browser's agent string from cherrypy"""
        return cherrypy.request.headers["User-Agent"]