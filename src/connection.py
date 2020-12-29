class Connection:

    def __init__(self, socket):
        self.socket = socket

    def send(self, serializable):
        self.socket.send(serializable.serialize())

    def receive(self):
        type_id = self.socket.recv(1)[0]
