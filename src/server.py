# -*- coding: utf-8 -*-

import http.server


class HttpHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("content-length"))
        print('content_length = {}'.format(content_length))
        body = self.rfile.read(content_length).decode("utf-8")
        print('body = {}'.format(body))
        body = 'Hello, world!'
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body.encode()))
        self.end_headers()
        self.wfile.write(body.encode())


if __name__ == '__main__':
    host = ''
    port = 80
    httpd = http.server.HTTPServer((host, port), HttpHandler)
    print('server started: %s' % port)
    httpd.serve_forever()
