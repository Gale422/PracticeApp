import json
from pathlib import Path

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "http://localhost:3000")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")


class MainHandler(BaseHandler):
    def prepare(self):
        self.render("index.html")


class DataHandler(BaseHandler):
    def get(self):
        search = self.get_argument('search', None)
        print("search={}".format(search))
        file_path = Path(__file__).parents[3] / 'contents' / 'testData.json'
        file_data = open(file_path, 'r')
        data_list = json.load(file_data)
        print('data_list: {}'.format(json.dumps(data_list,indent=2)))
        self.write(json.dumps(data_list))
