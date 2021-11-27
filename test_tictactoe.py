import unittest
from tictactoe import TicTacToe
from unittest.mock import Mock, MagicMock, patch

mock = Mock()

class TestUtils(unittest.TestCase):

    def test_place_marker(self):
        self.tictac3 = TicTacToe
        placed_marker = self.tictac3.place_marker(MagicMock,"x",0,0)
        self.assertEqual(placed_marker,"NAUGHT_TURN")


if __name__ == '__main__':
    unittest.main()
