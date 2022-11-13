import http.server as server
import json

port = 16649

class DaemonServer(server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(0)
    def do_POST(self):
        content_len = int(self.headers["Content-Length"])
        #data = json.load(self.rfile.read(content_len))
        data = self.rfile.read(content_len)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        print(data)
        self.wfile.write(bytes(data))

server=server.HTTPServer(("localhost", port), DaemonServer)

print("Server online!")
server.serve_forever()
server.server_close()
print("Server closed!")