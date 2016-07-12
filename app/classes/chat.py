# -*- coding: utf-8 -*-

from ..settings import bot

class Chat(object):

    def __init__(self, chat_id, text=''):
        self.chat_id = chat_id
        self.text = text

    # main process method
    def process(self):
        bot.sendMessage(chat_id=self.chat_id, text=u"> {}".format(self.text))
