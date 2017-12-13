from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

class HelloHandler(RequestHandler):
    def get(self):
        username = self.get_argument('user')
        str_out = "Hello, " + username
        self.write(str_out)

if __name__ == "__main__":
    handler_mapping = [(r'/', HelloHandler),]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()
