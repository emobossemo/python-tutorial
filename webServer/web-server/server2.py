#-*- coding:utf-8 -*-

import sys, os, BaseHTTPServer

class ServerException(Exception):
    pass

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    Error_Page = '''
    <html>
        <body>
            <h1>Error accessing {path}</h1>
            <p>{msg}</p>
        </body>
    </html>


    '''


    def do_GET(self):

        try:
            #文件完整路径
            full_path = os.getcwd() + self.path

            if not os.path.exists(full_path):
                raise  ServerException("'{0}' not found".format(self.path))

            elif os.path.isfile(full_path):

                self.handle_file(full_path)

            else:
                raise  ServerException("Unknow object '{0}'".format((self.path)))

        except Exception as msg:
            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path = self.path, msg = msg)
        self.send_content(content, 404)

    def send_content(self, content, status=200):

        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def handle_file(self, full_):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)

        except IOError as msg:

            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

#判断是否是直接运行该.py文件,
# 在cmd 中直接运行.py文件,则__name__的值是__main__,
# 而该.py文件被import到其他.py文件中,该.py文件的__name__值就不是__main__,而是其文件名
if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
