import cherrypy
import os
import telebot

token = "320545030:AAF8okRjCqGkFoylEamUGuN4V9v60StAvgQ"

WEBHOOK_HOST = '0.0.0.0'
WEBHOOK_PORT = 5000
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (token)

bot = telebot.TeleBot(token)
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
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)




cherrypy.config.update({
    'server.socket_host': '0.0.0.0',
    'server.socket_port': int(os.environ.get('PORT', 5000)),
})


cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/bot': {}})