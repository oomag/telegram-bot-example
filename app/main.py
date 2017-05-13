#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import telebot
import cherrypy
import config
import cherryconf

bot = telebot.TeleBot(config.token)










cherrypy.config.update({
    'server.socket_host': cherryconf.WEBHOOK_LISTEN,
    'server.socket_port': cherryconf.WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': cherryconf.WEBHOOK_SSL_CERT,
    'server.ssl_private_key': cherryconf.WEBHOOK_SSL_PRIV
})


cherrypy.quickstart( )