import http.server

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Set the required headers
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        super().end_headers()

# Start the server
if __name__ == "__main__":
    server_address = ('', 8000)  # Serve on port 8000
    httpd = http.server.HTTPServer(server_address, CustomHTTPRequestHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
