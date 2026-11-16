"""Local test server (WebGL cannot load textures from file://).  python serve.py  ->  http://localhost:8000"""
import http.server,socketserver,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with socketserver.TCPServer(("",8000),http.server.SimpleHTTPRequestHandler) as h:
    print("Open http://localhost:8000");h.serve_forever()
