from c4_lib import c4_io, c4_engine
import unittest


class TestGame(unittest.TestCase):

    # Testing Horizontal
    def test_win_hor_01(self):
        g1 = c4_engine.Game(7, 8, 4)
        g1.board[0][0] = 0
        g1.board[0][1] = 0
        g1.board[0][2] = 0
        g1.board[0][3] = 0
        answer = g1.check_winner()
        self.assertEqual(answer, 0)

    def test_win_hor_top(self):
        g1 = c4_engine.Game(6, 6, 5)
        num_rows = 6
        g1.board[num_rows - 1][0] = 0
        g1.board[num_rows - 1][1] = 0
        g1.board[num_rows - 1][2] = 0
        g1.board[num_rows - 1][3] = 0
        g1.board[num_rows - 1][4] = 0
        answer = g1.check_winner()
        self.assertEqual(answer, 0)

    def test_win_hor_top_full(self):
        g1 = c4_engine.Game(5, 5, 5)
        num_rows = 5
        g1.board[num_rows - 1][0] = 1
        g1.board[num_rows - 1][1] = 1
        g1.board[num_rows - 1][2] = 1
        g1.board[num_rows - 1][3] = 1
        g1.board[num_rows - 1][4] = 1
        answer = g1.check_winner()
        self.assertEqual(answer, 1)

    def test_win_hor_top_fail(self):
        g1 = c4_engine.Game(5, 5, 5)
        num_rows = 5
        g1.board[num_rows - 1][0] = 1
        g1.board[num_rows - 1][1] = 1
        g1.board[num_rows - 1][2] = 1
        g1.board[num_rows - 1][3] = 1
        answer = g1.check_winner()
        self.assertEqual(answer, -1)

    def test_win_hor_top_overload(self):
        g1 = c4_engine.Game(5, 5, 2)
        num_rows = 5
        g1.board[num_rows - 1][0] = 1
        g1.board[num_rows - 1][1] = 1
        g1.board[num_rows - 1][2] = 1
        g1.board[num_rows - 1][3] = 1
        answer = g1.check_winner()
        self.assertEqual(answer, 1)

    def test_win_hor_top_double(self):
        g1 = c4_engine.Game(20, 20, 2)
        num_rows = 20
        g1.board[0][num_rows - 1] = 1
        g1.board[0][num_rows - 2] = 1
        answer = g1.check_winner()
        self.assertEqual(answer, 1)

    def test_win_hor_top_single_fail(self):
        g1 = c4_engine.Game(5, 5, 1)
        num_rows = 5
        g1.board[2][3] = 1
        answer = g1.check_winner()
        self.assertEqual(answer, -1)

    # Testing Vertical
    def test_win_vert_right_full(self):
        g1 = c4_engine.Game(6, 6, 6)
        num_columns = 6
        g1.board[0][num_columns - 1] = 0
        g1.board[1][num_columns - 1] = 0
        g1.board[2][num_columns - 1] = 0
        g1.board[3][num_columns - 1] = 0
        g1.board[4][num_columns - 1] = 0
        g1.board[5][num_columns - 1] = 0
        answer = g1.check_winner()
        self.assertEqual(answer, 0)

    def test_win_vert_mid(self):
        g1 = c4_engine.Game(6, 6, 3)
        num_columns = 6
        g1.board[2][num_columns - 4] = 0
        g1.board[3][num_columns - 4] = 0
        g1.board[4][num_columns - 4] = 0
        g1.board[5][num_columns - 4] = 0
        answer = g1.check_winner()
        self.assertEqual(answer, 0)

    def test_win_vert_right_double(self):
        g1 = c4_engine.Game(6, 6, 2)
        num_columns = 6
        g1.board[0][0] = 0
        g1.board[1][0] = 0
        answer = g1.check_winner()
        self.assertEqual(answer, 0)

    # Testing Right Diag
    def test_win_rightdiag_double(self):
        g1 = c4_engine.Game(4, 4, 2)
        num_rows = 4
        g1.board[2][2] = 1
        g1.board[3][3] = 1
        answer = g1.check_winner()
        self.assertEqual(answer, 1)

    def test_win_rightdiag_top_right(self):
        g1 = c4_engine.Game(7, 7, 5)
        num_rows = 7
        g1.board[2][2] = 0
        g1.board[3][3] = 0
        g1.board[4][4] = 0
        g1.board[5][5] = 0
        g1.board[6][6] = 0
        answer = g1.check_winner()
        self.assertEqual(answer, 0)

    # Testing Left Diag
    def test_win_leftdiag_full(self):
        g1 = c4_engine.Game(4, 4, 4)
        num_rows = 4
        g1.board[num_rows - 1][0] = 1
        g1.board[num_rows - 2][1] = 1
        g1.board[num_rows - 3][2] = 1
        g1.board[num_rows - 4][3] = 1
        answer = g1.check_winner()
        self.assertEqual(answer, 1)

    def test_win_leftdiag_double(self):
        g1 = c4_engine.Game(7, 7, 2)
        num_rows = 7
        g1.board[num_rows - 1][0] = 0
        g1.board[num_rows - 2][1] = 0
        answer = g1.check_winner()
        self.assertEqual(answer, 0)


if __name__ == '__main__':
    unittest.main()
