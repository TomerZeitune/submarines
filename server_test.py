from src.server.server import Server
from src.game.game import Game
from src.core.constants import SUB, SEA


def main():
    table = [[SUB, SUB, SUB, SEA, SEA, SEA, SEA, SEA, SEA, SEA],
             [SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA],
             [SUB, SEA, SEA, SUB, SEA, SUB, SUB, SUB, SUB, SEA],
             [SUB, SEA, SEA, SUB, SEA, SEA, SEA, SEA, SEA, SEA],
             [SUB, SEA, SEA, SUB, SEA, SEA, SEA, SEA, SEA, SEA],
             [SUB, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA],
             [SUB, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA],
             [SEA, SEA, SEA, SUB, SUB, SUB, SUB, SEA, SEA, SUB],
             [SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SUB],
             [SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SEA, SUB]]

    server = Server(5555)
    server.begin()
    Game(server, table, True).play()
    server.end()


if __name__ == "__main__":
    main()

