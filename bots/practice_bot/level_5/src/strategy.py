from .hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random

class Strategy():

    def __init__(self, game_map, parameters, ownerId):
        self.game_map = game_map
        self.parameters = parameters
        self.ownerId = ownerId


    def decide_move(self, square):
        direction = self._find_can_eat_direction(square)
        if direction:
            return Move(square, direction)
        if self._should_stay_still(square):
            return Move(square, STILL)
        direction = self._find_best_border_direction(square)
        return Move(square, direction)

    def _find_best_border_direction(self, square):
        foreign_squares = [square for square in self.game_map if square.owner != self.ownerId]
        foreign_squares.sort( key=lambda fs: fs.production, reverse=True)
        foreign_squares = foreign_squares[0:50]
        closest_foreign_square = min(foreign_squares, key=lambda fs: self.game_map.get_distance(fs, square))
        direction = self._find_direction_to_target(square, closest_foreign_square)
        return direction

    def _find_direction_to_target(self, source_square, target_square):
        directions = {0: NORTH, 1: EAST, 2: SOUTH, 3: WEST}
        neighbors = self.game_map.neighbors(source_square)
        distance_direction_list = list()
        for key in directions:
            neighbour = next(neighbors)
            distance = self.game_map.get_distance(target_square, neighbour)
            distance_direction_list.append((distance, directions[key]))
        return min(distance_direction_list)[1]


    def _find_can_eat_direction(self, square):
        directions = {0: NORTH, 1: EAST, 2: SOUTH, 3: WEST}
        neighbors = self.game_map.neighbors(square)
        for key in directions:
            neighbour = next(neighbors)
            if ((neighbour.strength < square.strength) and (neighbour.owner != square.owner)):
                return directions[key]
        return None


    def _should_stay_still(self, square):
        return square.strength <= self.parameters.STRENGTH_THRESHOLD



