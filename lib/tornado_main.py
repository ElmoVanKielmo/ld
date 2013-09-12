#!/usr/bin/python

from threading import Thread
from tornado.options import define, options
from tornado.web import FallbackHandler, Application, StaticFileHandler
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from wsgi import application as django_app
from settings import PROJECT_ROOT
from dbus_api import DBusApi


def run():
    try:
        define("addr", default="127.0.0.1", help="Address to listen on")
        define("port", default="8000", help="Port to listen on")
        dbus_thread = Thread(target=DBusApi.run_me)
        dbus_thread.daemon = False
        dbus_thread.start()
        wsgi_app = WSGIContainer(django_app)
        application = Application([
            (
                r"/static/(.*)",
                StaticFileHandler,
                {"path": PROJECT_ROOT + "/static"}
            ),
            (r".*", FallbackHandler, dict(fallback=wsgi_app))
        ])
        application.listen(options.port, options.addr)
        IOLoop.instance().start()
    except KeyboardInterrupt:
        print 'Shutting down...'
        DBusApi.shutdown_event.set()
        dbus_thread.join()
        print 'Exit on user demand OK'


if __name__ == "__main__":
    run()
