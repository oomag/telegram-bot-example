import telegram
import json
import traceback
from ..classes import Chat

class HookResource(object):
    def on_post(self, req, resp):
        try:
            body = req.stream.read()
            body_decoded = body.decode("utf-8")
            json_body = json.loads(body_decoded)

            update = telegram.Update.de_json(json_body)

            chat_id = update.message.chat.id
            text = update.message.text

            chat = Chat(chat_id, text)
            chat.process()

        except Exception as e:
            traceback.print_exc()
