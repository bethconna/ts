import logging
import os

import webob.dec
import webob.exc

from paste.deploy import loadapp
from wsgiref.simple_server import make_server

import routes.middleware


LOG = logging.getLogger(__name__)


class Controller(object):
    @webob.dec.wsgify
    def __call__(self, req):
        arg_dict = req.environ['wsgiorg.routing_args'][1]
        action = arg_dict.pop('action')

        return webob.Response('OK')

    def getMessage(self, context, user_id):
        return {'Message': 'TestMessage'}


class Router(object):
    def __init__(self):
        self._mapper = routes.Mapper()
        self._mapper.connect('/test/{user_id}',
                             controller=Controller(),
                             action='getMessage',
                             conditions={'method': ['GET']})
        print(self._dispatch)
        self._router = routes.middleware.RoutesMiddleware(self._dispatch, self._mapper)


    @webob.dec.wsgify
    def __call__(self, req):
        return self._router

    @staticmethod
    @webob.dec.wsgify
    def _dispatch(req):
        match = req.environ['wsgiorg.routing_args'][1]

        if not match:
            return webob.exc.HTTPNotFound()

        app = match['controller']
        return app

    @classmethod
    def app_factory(cls, global_config, **local_config):
        return cls()


if __name__ == '__main__':
    configfile = 'tsroutes.ini'
    appname = "main"
    # wsgi_app是URLMap对象
    path = os.path.abspath(configfile)
    wsgi_app = loadapp("config:%s" % path, appname)
    httpd = make_server('localhost', 8282, wsgi_app)
    httpd.serve_forever()