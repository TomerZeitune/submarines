from src.server.server import Server
from src.game.game import Game

server = Server(5555)
server.begin()
Game(server, True).play()
server.end()
