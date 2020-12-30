from src.client.client import Client
from src.server.server import Server
from game import Game
from src.core.logging import Logger


def main():
    peer = Server(5555)
    peer.begin()
    Game().play(True)
    peer.end()


if __name__ == "__main__":
    main()
