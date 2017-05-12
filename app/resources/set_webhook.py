import falcon
from ..settings import WEBHOOK_URL, bot

class SetWebhookResource(object):
    def __init__(self):
        self.bot = bot

    def on_get(self, req, resp, **params):
        s = self.bot.setWebhook(WEBHOOK_URL)
        if s:
            resp.body = 'ok'
            resp.status = falcon.HTTP_200
        else:
            resp.body = 'an error occured'
            resp.status = falcon.HTTP_500

