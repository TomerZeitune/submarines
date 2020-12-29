from ..client.client import Client
from ..server.server import Server
from game import Game


def main():
    Game(Client("localhost", 5555)).play(True)


if __name__ == "__main__":
    main()
