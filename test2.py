import cherrypy
import os
import telebot

token = "374526741:AAGzUUxN2t9SkMXLHeA2YXuRsQf78cYGyhk"
bot = telebot.TeleBot(token)
class StringMaker(object):
    @cherrypy.expose
    def index(self):
        token = "374526741:AAGzUUxN2t9SkMXLHeA2YXuRsQf78cYGyhk"
        bot = telebot.TeleBot(token)
        @bot.message_handler(content_types=["text"])
        def handle_text(message):
            bot.send_message(message.from_user.id, message.text)

        bot.polling(none_stop=True, interval=0)

cherrypy.config.update({
    'server.socket_host': '0.0.0.0',
    'server.socket_port': int(os.environ.get('PORT', 5000)),
})


cherrypy.quickstart(StringMaker())