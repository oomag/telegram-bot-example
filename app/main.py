#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import telebot
import cherrypy
import config
import cherryconf

bot = telebot.TeleBot(config.token)



class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)

            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)





bot.remove_webhook()


bot.set_webhook(url=cherryconf.WEBHOOK_URL_BASE + cherryconf.WEBHOOK_URL_PATH,
                certificate=open(cherryconf.WEBHOOK_SSL_CERT, 'r'))


cherrypy.config.update({
    'server.socket_host': cherryconf.WEBHOOK_LISTEN,
    'server.socket_port': cherryconf.WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': cherryconf.WEBHOOK_SSL_CERT,
    'server.ssl_private_key': cherryconf.WEBHOOK_SSL_PRIV
})


cherrypy.quickstart(WebhookServer(), cherryconf.WEBHOOK_URL_PATH, {'/app': {}})