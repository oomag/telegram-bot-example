import telebot

BOT_TOKEN = '374526741:AAGzUUxN2t9SkMXLHeA2YXuRsQf78cYGyhk'
WEBHOOK_URL = 'https://mybots1.dokkurapp.com/HOOK'
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)