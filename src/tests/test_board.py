import unittest
from src.board import *

class TestBoard(unittest.TestCase):
    def test_width(self):
        self.assertEqual(WIDTH, 900)

    def test_height(self):
        self.assertEqual(HEIGHT, 700)

    def test_width(self):
        self.assertEqual(TETRIS_WIDTH, 300)

    def test_height(self):
        self.assertEqual(TETRIS_HEIGHT, 600)

    def test_block_size(self):
        self.assertEqual(BLOCK_SIZE, 30)

    def test_left_x(self):
        self.assertEqual(LEFT_X, (WIDTH - TETRIS_WIDTH) // 2)

    def test_left_y(self):
        self.assertEqual(LEFT_Y, HEIGHT - TETRIS_HEIGHT)

    def test_shapes(self):
        self.assertIsInstance(shapes, list)
        self.assertGreater(len(shapes), 0)

    def test_shape_colors(self):
        self.assertIsInstance(shape_colors, list)
        self.assertGreater(len(shape_colors), 0)

if __name__ == '__main__':
    unittest.main()