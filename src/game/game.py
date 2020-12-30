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
    def __print_table(self):
        for i in range(0, len(self.table)):
            for j in range(0, len(self.table[0])):
                print({True: " X ", False: " # "}[self.table[i][j]], end="")
            print()

    def __defend(self):
        self.__print_table()
        print("Waiting for enemy to make a move...")
        message = self.peer.connection().receive()
        if message.type_id == MessageType.ATTACK_SUBMARINE:
            print(f"Enemy attacked {message.data[0]}, {message.data[1]}")
            if self.table[message.data[0]][message.data[1]]:
                print("Your submarine was hit")
                self.peer.connection().send(Message(MessageType.YES, []))
                self.table[message.data[0]][message.data[1]] = False
            else:
                print("All good!")
                self.peer.connection().send(Message(MessageType.NO, []))
        self.__is_over = reduce(lambda acc, elem: acc or elem, self.table, False)

    def __attack(self):
        print("- Time to attack -")
        column, row = input("Enter column index: "), input("Enter row index: ")
        self.peer.connection().send(Message(MessageType.ATTACK_SUBMARINE, [column, row]))
        result = self.peer.connection().receive()
        if result.type_id == MessageType.NO:
            print("Missed!")
        elif result.type_id == MessageType.YES:
            print("Hit!")
        elif result.type_id == MessageType.SUBMARINE_SINK:
            print("You sunk a submarine!")
            self.enemy_submarine_count -= 1
            if self.enemy_submarine_count <= 0:
                self.__is_over = True

    def play(self):
        print("Welcome to submarines!")
        while not self.__is_over():
            if self.attacking:
                self.__attack()
            else:
                self.__defend()
