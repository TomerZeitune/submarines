from src.core.message import Message
from src.core.constants import MessageType
from functools import reduce


class Game:
    def __init__(self, peer, attacking):
        self.peer = peer
        self.attacking = attacking
        self.table = [[False for _ in range(0, 10)] for _ in range(0, 10)]
        self.enemy_submarine_count = 5
        self.__is_over = False

    # TODO ADD RANDOM FILL WITH SUBMARINES

    def __defend(self):
        message = self.peer.connection().receive()
        if message.type_id == MessageType.ATTACK_SUBMARINE:
            if self.table[message.data[0]][message.data[1]]:
                self.peer.connection().send(Message(MessageType.YES, []))
                self.table[message.data[0]][message.data[1]] = False
            else:
                self.peer.connection().send(Message(MessageType.NO, []))
        self.__is_over = reduce(lambda acc, elem: acc or elem, self.table, False)

    def __attack(self):
        self.peer.connection().send(Message(MessageType.ATTACK_SUBMARINE, [0, 0]))
        result = self.peer.connection().receive()
        if result.type_id == MessageType.NO:
            pass
        elif result.type_id == MessageType.YES:
            pass
        elif result.type_id == MessageType.SUBMARINE_SINK:
            self.enemy_submarine_count -= 1
            if self.enemy_submarine_count <= 0:
                self.__is_over = True

    def play(self):
        self.peer.begin()
        while not self.__is_over():
            if self.attacking:
                self.__attack()
            else:
                self.__defend()
