import unittest
from src.parameters import Parameters
from src.strategy import Strategy
from src.hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square

STRENGTH_THRESHOLD = 10

class TestBasicStrategies(unittest.TestCase):



    def setUp(self):
        parameters = Parameters()
        parameters.STRENGTH_THRESHOLD = STRENGTH_THRESHOLD
        self.strategy = Strategy(None, parameters)


    def test_whenStrengthUnderThreshold_thenStayStill(self):
        square = Square(0, 0, None, STRENGTH_THRESHOLD-1, None)
        move = self.strategy.decide_move(square)
        self.assertEqual(Move(square, STILL), move)


