# -*- coding: utf-8 -*-

import http.server
import json
import requests

class HttpHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("content-length"))
        print('content_length = {}'.format(content_length))
        body = self.rfile.read(content_length).decode("utf-8")
        print('body = {}'.format(body))
        try:
            body = json.loads(body)
            contents = self._get_changed_file(body)
        except json.decoder.JSONDecodeError as e:
            pass
        body = 'Hello, world!'
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body.encode()))
        self.end_headers()
        self.wfile.write(body.encode())

    def _get_changed_file(self, body):
        access_token = body.get('token', {}).get('read', {}).get('access_token')
        src = body.get('source', {})
        id_ = src.get('id')
        name = src.get('name')
        print('access_token = {}'.format(access_token))
        print('file = {}({})'.format(name, id_))
        url = 'https://api.box.com/2.0/files/{}/content/'.format(id_)
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        contents = r.text
        print('contens = {}'.format(contents))
        return contents


if __name__ == '__main__':
    host = ''
    port = 80
    httpd = http.server.HTTPServer((host, port), HttpHandler)
    print('server started: %s' % port)
    httpd.serve_forever()
