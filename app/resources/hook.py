import telebot
import json
import traceback
from ..classes import Chat
from ..settings import bot

class HookResource(object):
    def on_post(self, req, resp):
        try:
            body = req.stream.read()
            body_decoded = body.decode("utf-8")
            json_body = json.loads(body_decoded)

            update = bot.get_updates(json_body)

            chat_id = update.chat_id
            text = update.message.text

            chat = Chat(chat_id, text)
            chat.process()

        except Exception as e:
            traceback.print_exc()
