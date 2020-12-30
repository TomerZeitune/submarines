from src.client.client import Client
from src.game.game import Game
from src.core.constants import SUB, SEA


def main():
    table = [[SUB, SUB, SUB, SEA, SUB, SUB, SUB, SEA, SEA, SEA],
             [SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA],
             [SUB, SEA, SEA, SEA, SEA, SUB, SUB, SUB, SUB, SEA],
             [SUB, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA],
             [SUB, SEA, SEA, SUB, SUB, SUB, SEA, SEA, SEA, SEA],
             [SUB, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA],
             [SUB, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA],
             [SEA, SEA, SEA, SUB, SUB, SUB, SUB, SEA, SEA, SEA],
             [SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA],
             [SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA]]

    client = Client("127.0.0.1", 5555)
    client.begin()
    Game(client, table, False).play()
    client.end()


if __name__ == "__main__":
    main()
