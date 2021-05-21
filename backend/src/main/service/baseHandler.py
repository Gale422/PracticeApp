#!/bin/env python
# -*- coding: utf-8 -*-
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        origin = self.request.headers.get("Origin")
        valid_origin_list = [
            "http://127.0.0.1",
            "http://127.0.0.1:80",
            "http://127.0.0.1:3000",
            "http://127.0.0.1:8888",
            "http://localhost",
            "http://localhost:80",
            "http://localhost:3000",
            "http://localhost:8888"
        ]
        print(origin + " is " +
              "valid origin" if origin in valid_origin_list else "invalid origin")
        print(self.request)
        if origin in valid_origin_list:
            self.set_header("Access-Control-Allow-Origin", origin)
            self.set_header("Access-Control-Allow-Headers",
                            "origin, x-requested-with, Content-Type")
            self.set_header('Access-Control-Allow-Methods',
                            'POST,GET,PUT,DELETE,OPTIONS')

    def options(self):
        pass
