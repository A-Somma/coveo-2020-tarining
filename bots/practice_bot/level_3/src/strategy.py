from .hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random

class Strategy():

    def __init__(self, game_map, parameters):
        self.game_map = game_map
        self.parameters = parameters


    def decide_move(self, square):
        if self._should_stay_still(square):
            return Move(square, STILL)
        direction = self._find_best_direction(square)
        return Move(square, direction)

    def _find_best_direction(self, square):
        directions = {0: NORTH, 1: EAST, 2: SOUTH, 3: WEST}
        neighbors = self.game_map.neighbors(square)
        for key in directions:
            neighbour = next(neighbors)
            if ((neighbour.strength < square.strength) and (neighbour.owner != square.owner)):
                return directions[key]
        return random.choice((NORTH, EAST))

    def _should_stay_still(self, square):
        return square.strength <= self.parameters.STRENGTH_THRESHOLD



