#!/bin/env python
# -*- coding: utf-8 -*-
from .baseHandler import BaseHandler
from .domain.dbConnector import DbConnector
from datetime import datetime
import json


def json_datetime_serial(obj):
    # datetime型のみ処理対象とする
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError(repr(o) + " is not JSON serializable")


class DataHandler(BaseHandler):
    def get(self):
        # search = self.get_argument('search', None)
        # print("search={}".format(search))
        result = DbConnector().getToDoAll()
        self.write(json.dumps(result, default=json_datetime_serial))


class ToDoDetailHandler(BaseHandler):
    def post(self):
        self.write("test")

    def get(self):
        toDoId = self.get_argument('id', None)
        result = DbConnector().getToDoDetailByToDoId(toDoId)
        self.write(json.dumps(result, default=json_datetime_serial))

class TagsHandler(BaseHandler):
    def get(self):
        self.write(json.dumps(DbConnector().getTagAll(), default=json_datetime_serial))