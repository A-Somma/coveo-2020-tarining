from .hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random

class Strategy():

	def __init__(self, game_map, parameters):
		self.game_map = game_map
		self.parameters = parameters


	def decide_move(self, square):
		if self._should_stay_still(square):
			return Move(square, STILL)
		return Move(square, random.choice((NORTH, EAST)))

	def _should_stay_still(self, square):
		return square.strength <= self.parameters.STRENGTH_THRESHOLD



