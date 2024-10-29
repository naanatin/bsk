import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame

class TestBowlingGame(unittest.TestCase):

    def test_create_game_10_frames(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        self.assertIsNotNone(game.get_frame_at(9))

    def test_11_frames_should_raise_bowling_error(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        self.assertRaises(BowlingError, game.add_frame, Frame(1, 5))

    def test_count_came_score(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        self.assertEqual(81, game.calculate_score())

    def test_count_game_score_with_one_spare(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 9))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        self.assertEqual(88, game.calculate_score())

    def test_count_game_score_with_two_spares(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 9))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 2))
        game.add_frame(Frame(2, 6))

        self.assertEqual(91, game.calculate_score())