from pathlib import Path
from .baseHandler import BaseHandler
from .domain.dbConnector import DbConnector
import json


class MainHandler(BaseHandler):
    def prepare(self):
        self.render("index.html")


class DataHandler(BaseHandler):
    def get(self):
        # search = self.get_argument('search', None)
        # print("search={}".format(search))
        result = DbConnector().getAll()
        self.write(json.dumps(result))
