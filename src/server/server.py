import socket
from src.core.connection import Connection
from src.core.constants import MessageType, MAX_CONNECT_REQUEST
from src.core.message import Message
from src.core.exceptions import UnexpectedMessageError


class Server:
    def __init__(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("0.0.0.0", port))
        sock.listen(MAX_CONNECT_REQUEST)
        self.__connection = Connection(sock.accept())

# TODO Fix AttributeError: 'tuple' object has no attribute 'recv'
    
    def begin(self):
        message = self.connection().receive()
        if message.type_id == MessageType.BEGIN_SESSION:
            self.connection().send(Message(MessageType.READY, []))
            return
        elif message.type_id == MessageType.CONTINUE_SESSION:
            self.connection().send(Message(MessageType.NO, []))
            return
        raise UnexpectedMessageError()

    def connection(self):
        return self.__connection

    def end(self):
        self.connection().send(Message(MessageType.DISCONNECT, []))
