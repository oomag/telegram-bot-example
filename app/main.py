import falcon
from resources import HookResource, SetWebhookResource, MainResource

api = falcon.API()
api.add_route('/', MainResource())
api.add_route('/HOOK', HookResource())
api.add_route('/set_webhook', SetWebhookResource())
