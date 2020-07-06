import socket # tcp library
import socketserver # simplifies the creation of the tcp server
import sys
from decouple import config

host = config('HOST')
port = config('PORT', cast=int)
message_size = config('MESSAGE_SIZE', cast=int)

class VantageProtocolRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:

            payload = self.request.recv(message_size).strip()
            if not payload:
                break

            print("Received from {0}: {1}".format(self.request.getsockname(), payload))

def main():

    server = socketserver.ThreadingTCPServer((host, port), VantageProtocolRequestHandler)
    server.serve_forever()
    server.server_close()
       

if __name__ == "__main__":
    main()
