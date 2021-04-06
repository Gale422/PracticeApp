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
        self.write('{検索結果: [{test1}, {test2}]}')