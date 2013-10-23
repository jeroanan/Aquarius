import cherrypy

class web(object):

    def Main(self):
        cherrypy.config.update({'server.socket_port': 8080, 'server.socket_host:': 'localhost'})
        cherrypy.quickstart(webserver)
        
class webserver(object):
    pass


