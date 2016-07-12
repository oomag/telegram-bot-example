import falcon

class MainResource(object):
  def on_get(self, req, resp, **params):
    resp.body = u'hi, i\'m a bot'
    resp.status = falcon.HTTP_200
    resp.content_type = 'text/html'
