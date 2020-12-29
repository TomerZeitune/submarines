from ..core.message import Message
from ..core.constants import MessageType


class Game:
    def __init__(self, peer, attacking):
        self.peer = peer
        self.attacking = attacking
        self.table = [[False for _ in range(0, 10)] for _ in range(0, 10)]

    # TODO ADD RANDOM FILL WITH SUBMARINES

    def __is_over(self):
        for element in self.table:
            if element:
                return False
        return True

    def __defend(self):
        pass

    def __attack(self):
        self.peer.connection().send(Message(MessageType.ATTACK_SUBMARINE, [0, 0]))
        result = self.peer.connection().receive()
        if result.type_id == MessageType.NO:
            pass
        elif result.type_id == MessageType.YES:
            pass
        elif result.type_id == MessageType.SUBMARINE_SINK:
            pass
        pass

    def play(self):
        while not self.__is_over():
            if self.attacking:
                self.__attack()
            else:
                self.__defend()
