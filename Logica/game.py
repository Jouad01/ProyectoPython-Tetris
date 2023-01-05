import pygame
import random

from constantes import *

# con esta clase se crea las piezas que usaran otras funciones
# shape es la forma de la pieza, x y las coordenadas
class Piece(object):  
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

# crea una array de 20 filas y 10 columnas que representa el tablero del Tetris
# si la coordenada de la celda está en el diccionario locked_pos, se asigna el color de la celda desde el diccionario 
# de lo contrario, se asigna el color negro a la celda.
def create_grid(locked_pos={}):  # *
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j,i)]
                grid[i][j] = c
    return grid

# toma una pieza de Tetris como argumento y devuelve una lista de coordenadas que representan la forma de la pieza.
def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions

