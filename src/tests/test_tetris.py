import unittest
import pygame
import sys
sys.path.append('..')
from tetris import main

class TestTetris(unittest.TestCase):
    def test_main(self):
        pygame.init()
        win = pygame.display.set_mode((200, 200))
        main(win)
        self.assertFalse(pygame.display.get_init())

if __name__ == '__main__':
    unittest.main()
