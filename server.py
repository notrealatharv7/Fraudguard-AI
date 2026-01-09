from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

if __name__ == '__main__':
    web_dir = os.path.join(os.path.dirname(__file__), 'flutter_app/fraud_detector/build/web')
    os.chdir(web_dir)
    server_address = ('', int(os.environ.get('PORT', 8000)))
    httpd = HTTPServer(server_address, CORSRequestHandler)
    print(f'Serving on port {server_address[1]}...')
    httpd.serve_forever()