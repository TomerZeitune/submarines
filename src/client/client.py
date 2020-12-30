import socket
from src.core.connection import Connection
from src.core.message import Message
from src.core.constants import MessageType
from src.core.exceptions import DeniedError, UnexpectedMessageError
from src.core.logging import Logger


class Client:
    def __init__(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        self.__connection = Connection(sock)

    def begin(self):
        self.connection().send(Message(MessageType.BEGIN_SESSION, [0, 0]))
        message = self.connection().receive()
        if message.type_id == MessageType.YES:
            self.connection().send(Message(MessageType.READY, []))
            if self.connection().receive().type_id == MessageType.READY:
                return
        elif message.type_id == MessageType.NO:
            raise DeniedError("The server denied the request")
        raise UnexpectedMessageError()

    def connection(self):
        return self.__connection

    def end(self):
        self.connection().send(Message(MessageType.DISCONNECT, []))
