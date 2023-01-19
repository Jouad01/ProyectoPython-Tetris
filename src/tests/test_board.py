import unittest
from board import *

class TestBoard(unittest.TestCase):
    def test_width(self):
        self.assertEqual(WIDTH, 900)
    
    def test_height(self):
        self.assertEqual(HEIGHT, 700)
    
    def test_tetris_width(self):
        self.assertEqual(TETRIS_WIDTH, 300)

    def test_tetris_height(self):
        self.assertEqual(TETRIS_HEIGHT, 600)

    def test_block_size(self):
        self.assertEqual(BLOCK_SIZE, 30)
