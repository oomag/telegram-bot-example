import os
import telebot
import cherrypy
import time

token = "320545030:AAF8okRjCqGkFoylEamUGuN4V9v60StAvgQ"

WEBHOOK_HOST = '0.0.0.0'
WEBHOOK_PORT = int(os.environ.get('PORT', 5000))
WEBHOOK_LISTEN = '0.0.0.0'

bot = telebot.TeleBot(token)


class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        return 0


bot.remove_webhook()

time.sleep(5)


bot.set_webhook("https://myboot1.herokuapp.com/" + token)


cherrypy.config.update({
    'server.socket_host': '0.0.0.0',
    'server.socket_port': int(os.environ.get('PORT', 5000)),
})


cherrypy.quickstart(WebhookServer(), "https://myboot1.herokuapp.com/" + token)