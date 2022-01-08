import unittest
from tictactoe import TicTacToe


class TestUtils(unittest.TestCase):
    def test_place_marker(self):
        tictac = TicTacToe()
        tictac.create_board()
        cross_marker = tictac.place_marker("x", 0, 0)
        naught_marker = tictac.place_marker("o", 0, 1)
        self.assertEqual(cross_marker, "NAUGHT_TURN")
        self.assertEqual(naught_marker, "CROSS_TURN")

    def test_create_board(self):
        tictac1 = TicTacToe()
        tictac1.create_board()
        board_exists = tictac1.create_board()
        self.assertTrue(board_exists)

    def test_output_board(self):
        tictac2 = TicTacToe()
        tictac2.create_board()
        tictac2.place_marker("o", 0, 0)
        self.assertEqual(tictac2.output_board(), None)

    def test_check_winner(self):
        tictac3 = TicTacToe()
        tictac3.create_board()
        tictac3.place_marker("o", 0, 0)
        tictac3.place_marker("o", 0, 1)
        tictac3.place_marker("o", 0, 2)
        self.assertEqual(tictac3.check_winner(), "NAUGHT_WON")

    def test_check_draw(self):
        tictac4 = TicTacToe()
        tictac4.create_board()
        self.assertFalse(tictac4.check_draw())
        tictac4.place_marker("o", 0, 0)
        tictac4.place_marker("x", 1, 0)
        tictac4.place_marker("x", 2, 2)
        tictac4.place_marker("o", 2, 0)
        tictac4.place_marker("o", 2, 1)
        tictac4.place_marker("x", 1, 1)
        tictac4.place_marker("o", 1, 2)
        tictac4.place_marker("x", 0, 1)
        tictac4.place_marker("o", 0, 2)
        self.assertEqual(tictac4.check_draw(),"DRAW")


if __name__ == '__main__':
    unittest.main()
