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

    def deserialize(self, binary_data):
        type_id = unpack("B", binary_data[0:1])[0]
        data = []
        for i in range(1, len(binary_data), 2):
            data.append(unpack("h", binary_data[i:i+2])[0])
        return Message(type_id, data)
