import unittest
from board import *

class TestBoard(unittest.TestCase):
    def test_width(self):
        self.assertEqual(WIDTH, 900)