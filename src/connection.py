from constants import MessageType, MESSAGE_FIELDS_COUNTS, FIELD_SIZE
from message import Message
import socket

# TODO Test this code


class Connection:

    def __init__(self, connection_socket):
        self.sock = connection_socket

    def send(self, serializable):
        self.sock.send(serializable.serialize())

    def receive(self):
        type_id = self.sock.recv(1, socket.MSG_WAITALL)[0]
        binary_data = self.sock.recv(MESSAGE_FIELDS_COUNTS[type_id] * FIELD_SIZE, socket.MSG_WAITALL)
        return Message(type_id, binary_data)
