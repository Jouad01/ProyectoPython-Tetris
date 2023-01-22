import pygame
import sys
sys.path.append('..')
from game import *

def test_create_grid():
    locked_pos = {(1,1): (255,0,0)}
    grid = create_grid(locked_pos)
    assert grid[1][1] == (255,0,0)
    assert grid[0][0] == (0,0,0)

def test_check_lost():
    positions = [(0,0), (1,0), (2,0), (3,0)]
    assert check_lost(positions) == True

    positions = [(0,1), (1,1), (2,1), (3,1)]
    assert check_lost(positions) == False

def test_get_shape():
    shape = get_shape()
    assert shape.shape in shapes

def test_draw_text_middle():
    surface = pygame.Surface((100,100))
    text = "hola"
    size = 20
    color = (255,255,255)

def test_draw_grid():
    surface = pygame.Surface((100,100))
    grid = create_grid({})
    draw_grid(surface, grid)

def test_update_score():
    with open('../utilities/record.txt', 'w') as f:
        f.write("0")
        update_score(200)

def test_max_score():
    with open('../utilities/record.txt', 'w') as f:
        f.write("100")
        score = max_score()
