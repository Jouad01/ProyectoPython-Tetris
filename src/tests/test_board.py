import unittest
from board import *

class TestBoard(unittest.TestCase):
    def test_width(self):
        self.assertEqual(WIDTH, 900)
    
    def test_height(self):
        self.assertEqual(HEIGHT, 700)
        