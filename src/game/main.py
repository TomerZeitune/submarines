from src.client.client import Client
from src.server.server import Server
from game import Game


def main():
    Game(Client("localhost", 5555)).play(True)


if __name__ == "__main__":
    main()
