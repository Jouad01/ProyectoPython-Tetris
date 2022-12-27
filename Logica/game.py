# Crear clases: Piece, Board y Game

from Logica import constantes
import pygame
import random

pygame.init()
WINDOW_SIZE = (500, 1000)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tetris: Jouad & Noe")

class Piece:
    def __init__(self, x, y, blocks):
        self.x = x
        self.y = y
        self.blocks = blocks
    
    def move_right(self):
        self.x += 1
    
    def move_left(self):
        self.x -= 1
    
    def move_down(self):
        self.y += 1
    
    def rotar(self):
        # Pendiente de implementar
        pass

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.create_grid()
        self.level = 1
        self.score = 0
        self.points_level = 100
        self.speed = 500

    def create_grid(self, width):
        # Creamos una lista de listas para crear el tablero de juego. El tablero significa que cada cuadro es un 0
        grid = []
        for i in range(self.height):
            # Añadimos una lista vacia que representara una fila(???)
            grid.append([0] * width)
        return grid

    def añadir_piezas(self, pieces):
        for i in range(len(pieces.blocks)):
            for j in range(len(pieces.blocks[i])):
                if pieces.blocks[i][j] != 0:
                    self.grid[pieces.y + i][pieces.x + j] = pieces.blocks[i][j]

    def comprobar_filas(self):
        # Comprueba que todas las filas esten llenas 
        borrar_lineas = []
        for i in range(self.height):
            if all(self.grid[i]):
                borrar_lineas.append(i)
        if borrar_lineas:
            for fila in reversed(borrar_lineas):
                self.grid.pop(fila)
                # Añade una fila vacia al principio
                self.grid.insert(0, [0] * self.width)

        # Actualiza la puntuación y el nivel
        self.score = self.score + len(borrar_lineas) * 10
        self.actualizar_nivel()


    def actualizar_nivel(self):
        # Actualiza el nivel y la velocidad de caida de las piezas
        if self.score >= self.points_level:
            self.level += 1
            self.points_level += 100
            self.speed += 50

    def comprobar_gameover(self):
        # Recorre la primera fila de la matriz "grid" y se comprueba si hay algún elemento distinto de "0". 
        # Se recorre toda la fila y no se encuentra ningún elemento distinto de "0", se devuelve "False".
        for element in self.grid[0]:
            if element != 0:
                return True
        return False