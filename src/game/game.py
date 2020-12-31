import copy
from src.core.message import Message
from src.core.constants import MessageType, HIT, SEA, SUB


class Game:
    def __init__(self, peer, table, attacking):
        self.peer = peer
        self.attacking = attacking
        self.table = table
        self.enemy_submarine_count = 5
        self.__is_over = False

    def __print_table(self):
        for i in range(0, len(self.table)):
            for j in range(0, len(self.table[0])):
                print({SUB: " X ", SEA: " # ", HIT: " * "}[self.table[j][i]], end="")
            print()

    def __is_sank_submarine(self, table, column, row):
        if table[column][row] == SUB:
            return False
        elif table[column][row] == SEA:
            return True
        else:
            table[column][row] = SEA
            return self.__is_sank_submarine(table, column + 1, row) and\
                self.__is_sank_submarine(table, column - 1, row) and\
                self.__is_sank_submarine(table, column, row - 1) and\
                self.__is_sank_submarine(table, column, row + 1)

    def __defend(self):
        self.__print_table()
        print("Waiting for enemy to make a move...")
        message = self.peer.connection().receive()
        if message.type_id == MessageType.ATTACK_SUBMARINE:
            column, row = message.data[0], message.data[1]
            print(f"Enemy attacked {column}, {row}")
            if self.table[column][row]:
                print("Your submarine was hit")
                self.table[column][row] = HIT
                if self.__is_sank_submarine(copy.deepcopy(self.table), column, row):
                    self.peer.connection().send(Message(MessageType.SUBMARINE_SANK, [int(column), int(row), int(0)]))
                else:
                    self.peer.connection().send(Message(MessageType.YES, []))
            else:
                self.attacking = True
                print("All good!")
                self.peer.connection().send(Message(MessageType.NO, []))

    def __attack(self):
        print("- Time to attack -")
        column, row = input("Enter column index: "), input("Enter row index: ")
        self.peer.connection().send(Message(MessageType.ATTACK_SUBMARINE, [int(column), int(row)]))
        result = self.peer.connection().receive()
        if result.type_id == MessageType.NO:
            self.attacking = False
            print("Missed!")
        elif result.type_id == MessageType.YES:
            print("Hit!")
        elif result.type_id == MessageType.SUBMARINE_SANK:
            print("You sank a submarine!")
            self.enemy_submarine_count -= 1
            if self.enemy_submarine_count <= 0:
                print("You won!")
                self.__is_over = True

    def play(self):
        print("Welcome to submarines!")
        while not self.__is_over:
            if self.attacking:
                self.__attack()
            else:
                self.__defend()
                self.__is_over = True
                for row in self.table:
                    for column in row:
                        if column == SUB:
                            self.__is_over = False
                if self.__is_over:
                    print("You lost!")
