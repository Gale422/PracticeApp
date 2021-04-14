import json
from pathlib import Path

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        origin = self.request.headers.get("Origin")
        valid_origin_list = [
            "http://127.0.0.1",
            "http://127.0.0.1:80",
            "http://127.0.0.1:3000",
            "http://localhost",
            "http://localhost:80",
            "http://localhost:3000"
        ]
        print(origin + " is " + "valid origin" if origin in valid_origin_list else "invalid origin")
        if origin in valid_origin_list:
            self.set_header("Access-Control-Allow-Origin", origin)
            self.set_header("Access-Control-Allow-Headers", "x-requested-with")
            # self.set_header('Access-Control-Allow-Methods', 'POST, GET,　PUT, DELETE')


class MainHandler(BaseHandler):
    def prepare(self):
        self.render("index.html")


class DataHandler(BaseHandler):
    def get(self):
        # search = self.get_argument('search', None)
        # print("search={}".format(search))
        file_path = Path(__file__).parents[3] / 'contents' / 'testData.json'
        file_data = open(file_path, 'r')
        data_list = json.load(file_data)
        # print('data_list: {}'.format(json.dumps(data_list,indent=2)))
        self.write(json.dumps(data_list))
