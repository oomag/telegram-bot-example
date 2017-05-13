#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import os
import telebot
import config
from flask import Flask, request

server = Flask(__name__)
bot = telebot.TeleBot(config.token)


@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(config.url)
    return "!", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))











@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


