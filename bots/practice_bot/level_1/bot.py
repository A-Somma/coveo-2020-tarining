import src.hlt as hlt
from src.strategy import Strategy
from src.hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
from src.parameters import Parameters
import random

myID, game_map = hlt.get_init()
hlt.send_init("Level 1")
params = Parameters()

while True:
    game_map.get_frame()
    strategy = Strategy(game_map, params)
    moves = [strategy.decide_move(square) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)
