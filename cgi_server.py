#! /usr/bin/env python3
import os, sys, http.server
import html
server_address = ("localhost", 8080)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler

httpd = server(server_address, handler)
httpd.serve_forever()
