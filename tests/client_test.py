from src.client.client import Client
from src.game.game import Game


client = Client("127.0.0.1", 5555)
client.begin()
Game(client, False).play()
client.end()
