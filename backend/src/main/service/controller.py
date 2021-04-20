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
        file_path = Path(__file__).parents[3] / 'contents' / 'testData.json'
        file_data = open(file_path, 'r')
        data_list = json.load(file_data)
        result = DbConnector().getAll()
        # print('data_list: {}'.format(json.dumps(data_list,indent=2)))
        # self.write(json.dumps(data_list))
        self.write(json.dumps(result))
