import socket
from connection import Connection
from constants import MAX_CONNECT_REQUEST


class Server:
    def __init__(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((socket.gethostname(), port))
        sock.listen(MAX_CONNECT_REQUEST)
        self.connection = Connection(sock.accept())

    def begin(self):
        pass

    def connection(self):
        return self.connection

    def end(self):
        pass
