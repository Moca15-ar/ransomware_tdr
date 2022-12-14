from http.server import HTTPServer, BaseHTTPRequestHandler


class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('hello world'.encode())
        self.wfile.write(self.path[1:].encode())



def main():
    PORT = 8000
    server = HTTPServer(('', PORT), requestHandler) # hostname, port), request handler(get all requests the server receives)
    print('server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()