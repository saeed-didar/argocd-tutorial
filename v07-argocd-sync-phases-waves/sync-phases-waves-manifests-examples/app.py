from http.server import BaseHTTPRequestHandler, HTTPServer

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"running")

if __name__ == "__main__":
    server_address = ("", 5000)
    httpd = HTTPServer(server_address, HealthHandler)
    print("🚀 Demo app running on port 5000")
    httpd.serve_forever()
