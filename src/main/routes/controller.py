import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.render("index.html")