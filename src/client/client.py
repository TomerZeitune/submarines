import socket
from ..core.connection import Connection
from ..core.message import Message
from ..core.constants import MessageType
from ..core.exceptions import DeniedError, UnexpectedMessageError


class Client:
    def __init__(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        self.connection = Connection(sock)

    def begin(self):
        self.connection().send(Message(MessageType.BEGIN_SESSION, []))
        message = self.connection().receive()
        if message.type_id == MessageType.YES:
            self.connection().send(Message(MessageType.READY, []))
            return
        elif message.type_id == MessageType.NO:
            raise DeniedError("The server denied the request")
        raise UnexpectedMessageError()

    def connection(self):
        return self.connection

    def end(self):
        pass
