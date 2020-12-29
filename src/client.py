import socket
from connection import Connection


class Client:
    def __init__(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        self.connection = Connection(sock)

    def begin(self):
        pass

    def connection(self):
        return self.connection

    def end(self):
        pass
