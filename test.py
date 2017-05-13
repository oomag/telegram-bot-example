import cherrypy
import os

class StringMaker(object):
    @cherrypy.expose
    def index(self):
        return "Hello! How are you?"

cherrypy.config.update({
    'server.socket_host': '0.0.0.0',
    'server.socket_port': int(os.environ.get('PORT', 5000)),
})


cherrypy.quickstart(StringMaker())
