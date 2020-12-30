from src.core.constants import MessageType, MESSAGE_FIELDS_COUNTS, FIELD_SIZE
from src.core.message import Message
from src.core.logging import Logger
import socket
from struct import unpack


class Connection:

    def __init__(self, connection_socket):
        self.sock = connection_socket

    def send(self, serializable):

        binary_data = serializable.serialize()
        self.sock.send(binary_data)
        Logger.debug(f"Sent: {binary_data}")

    def receive(self):
        type_id = self.sock.recv(1, socket.MSG_WAITALL)[0]
        binary_data = self.sock.recv(MESSAGE_FIELDS_COUNTS[type_id] * FIELD_SIZE, socket.MSG_WAITALL)
        data = []
        for i in range(0, len(binary_data), FIELD_SIZE):
            data.append(unpack("h", binary_data[i:i + FIELD_SIZE])[0])
        Logger.debug(f"Received message: {type_id}, {data}")
        return Message(type_id, data)

    def __del__(self):
        self.sock.close()
