from src.hlt import NORTH, EAST, SOUTH, WEST, STILL, Square
from collections import namedtuple
import random

Neighbor = namedtuple('Neighbor', 'direction, neighbor')


class Strategy:

    def __init__(self, game_map, owner_id):
        self.game_map = game_map
        self.owner_id = owner_id

    def has_no_unoccupied_neighbor(self, neighbors):
        return len(list(filter(lambda neighbor: neighbor.owner == self.owner_id, neighbors))) == 0

    def apply_strategy(self, square):
        neighbors = self.game_map.neighbors(square)
        can_be_taken_neighbors = []
        neighbors2 = []
        for direction, neighbor in enumerate(neighbors):
            neighbors2.append(Neighbor(direction, neighbor))
            if square.strength > neighbor.strength and neighbor.owner != self.owner_id:
                can_be_taken_neighbors.append(Neighbor(direction, neighbor))

        if len(can_be_taken_neighbors) > 0:
            return max(can_be_taken_neighbors,
                       key=lambda neighbor_direction: neighbor_direction.neighbor.strength).direction
        elif self.has_no_unoccupied_neighbor(neighbors) and square.strength >= 80:
            return min(neighbors2, key=lambda neighbor_direction: neighbor_direction.neighbor.strength).direction
        elif square.strength == 255:
            return min(neighbors2, key=lambda neighbor_direction: neighbor_direction.neighbor.strength).direction
        else:
            return STILL
