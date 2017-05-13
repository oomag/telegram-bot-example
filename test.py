#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import os
import telebot
import config
from flask import Flask, request

token = '374526741:AAGzUUxN2t9SkMXLHeA2YXuRsQf78cYGyhk'

server = Flask(__name__)
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.send_message(message, message.text)

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url = "https://myboot1.herokuapp.com/bot")
    return "!", 200


server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))


