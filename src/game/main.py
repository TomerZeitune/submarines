from src.client.client import Client
from src.server.server import Server
from game import Game


def main():
    peer = Server(5555)
    peer.begin()
    Game().play(True)
    peer.end()


if __name__ == "__main__":
    main()
