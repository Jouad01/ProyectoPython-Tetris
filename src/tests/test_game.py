import pygame
import unittest
from game import *

class TestGame(unittest.TestCase):
    def test_Piece(self):
        piece = Piece(5, 0, "square")
        self.assertEqual(piece.x, 5)
        self.assertEqual(piece.y, 0)
        self.assertEqual(piece.shape, "square")
        self.assertEqual(piece.rotation, 0)

    def test_create_grid(self):
        locked_pos = {(1,1): (255,0,0)}
        grid = create_grid(locked_pos)
        self.assertEqual(grid[1][1], (255,0,0))
        self.assertEqual(grid[0][0], (0,0,0))

    def test_convert_shape_format(self):
        piece = Piece(5, 0, "square")
        shape_format = convert_shape_format(piece)
        self.assertEqual(shape_format[0], (3, -4))
        self.assertEqual(shape_format[1], (4, -4))
        self.assertEqual(shape_format[2], (3, -3))
        self.assertEqual(shape_format[3], (4, -3))

    def test_valid_space(self):
        piece = Piece(5, 0, "square")
        grid = create_grid()
        self.assertTrue(valid_space(piece, grid))

        piece = Piece(5, 19, "square")
        self.assertFalse(valid_space(piece, grid))

    def test_check_lost(self):
        positions = [(0,0), (1,0), (2,0), (3,0)]
        self.assertTrue(check_lost(positions))

        positions = [(0,1), (1,1), (2,1), (3,1)]
        self.assertFalse(check_lost(positions))

    def test_get_shape(self):
        shape = get_shape()
        self.assertIn(shape.shape, shapes)

    def test_draw_text_middle(self):
        surface = pygame.Surface((100,100))
        text = "hola"
        size = 20
        color = (255,255,255)
        draw_text_middle(surface, text, size, color)
        self.assertEqual(surface.get_at((50, 50)), color)

    def test_update_score(self):
        self.assertEqual(update_score(1), 100)
        self.assertEqual(update_score(2), 300)
        self.assertEqual(update_score(3), 700)
        self.assertEqual(update_score(4), 1500)

    def test_max_score(self):
        update_score(1)
        update_score(3)
        self.assertEqual(max_score(), 1500)
        update_score(4)
        self.assertEqual(max_score(), 1500)
        update_score(2)
        self.assertEqual(max_score(), 700)


if __name__ == '__main__':
    unittest.main()