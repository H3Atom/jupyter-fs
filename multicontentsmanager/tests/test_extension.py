# for Coverage
import tornado.web
from mock import MagicMock
from multicontentsmanager.extension import load_jupyter_server_extension, GetHandler


class TestExtension:
    def test_load_jupyter_server_extension(self):

        m = MagicMock()

        m.web_app.settings = {}
        m.web_app.settings['base_url'] = '/test'
        load_jupyter_server_extension(m)

    def test_get_handler(self):
        app = tornado.web.Application()
        m = MagicMock()
        h = GetHandler(app, m)
        h._transforms = []
        h.get()
