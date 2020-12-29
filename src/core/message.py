from struct import pack, unpack


class Message:
    def __init__(self, type_id, data):
        self.type_id = type_id
        self.data = data

    def serialize(self):
        binary_data = b""
        for element in self.data:
            binary_data += pack("h", element)
        return pack("B", self.type_id) + binary_data

