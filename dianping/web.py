import os
import sys
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
class AddAPIHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        page_links_line = self.get_argument("pll","")
        f = open(os.path.join(os.path.dirname(__file__),'static/files/%s.%s'%("shanghai","txt")), "ab")
        f.write(page_links_line.encode())
        f.write(",\n".encode())  # 多媒体存储content
        f.close()
        self.finish({})
class AddJsonAPIHandler(tornado.web.RequestHandler):
    def post(self):
        json_str = self.get_argument("json_str","{}")
        f = open(os.path.join(os.path.dirname(__file__),'static/files/%s.%s'%("result_json","txt")), "ab")
        f.write(json_str.encode())
        f.write(",\n".encode())  # 多媒体存储content
        f.close()
        self.finish({})
class DemoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("demo.html")
settings = {
    "debug":True
}
def make_app():
    return tornado.web.Application([
        (r"/demo",DemoHandler),
        (r"/api/add_json",AddJsonAPIHandler),
        (r"/api/add",AddAPIHandler),
        (r"/", MainHandler),
    ],
**settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()