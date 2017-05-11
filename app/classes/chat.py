# -*- coding: utf-8 -*-

from ..settings import bot

class Chat(object):

    def __init__(self, chat_id, text=''):
        self.chat_id = chat_id
        self.text = text

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)