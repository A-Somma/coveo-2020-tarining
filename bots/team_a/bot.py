import src.hlt as hlt
from src.hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square

from src.strategy import Strategy

myID, game_map = hlt.get_init()
hlt.send_init("Team A")

strategy = Strategy(game_map, myID)

while True:
    game_map.get_frame()
    moves = [Move(square, strategy.apply_strategy(square)) for square in game_map if
             square.owner == myID]
    hlt.send_frame(moves)
