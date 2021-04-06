#!/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import logging
import os
from pathlib import Path

import tornado.ioloop
import tornado.web
from tornado.options import define, options

from routes import controller

define("port", default=8888, type=int)


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", controller.MainHandler),
            (r"/data", controller.DataHandler),
        ]
        app_route = route_dirname()
        settings = dict(
            template_path=os.path.join(app_route,  "templates"),
            static_path=os.path.join(app_route,  "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def route_dirname():
    return Path(__file__).parents[2]


def setting_dirname():
    return os.path.join(route_dirname(), "settings")


def main():
    tornado.options.parse_config_file(
        os.path.join(setting_dirname(), "server.conf"))
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    logging.debug("run on port %d in %s mode" %
                  (options.port, options.logging))
    print("Server is start ...")
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
