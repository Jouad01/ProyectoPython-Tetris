# Crear clases: Piece, Board y Game

import Logica.constantes as constantes
import pygame # Se instala
import random
import numpy as np # Para rotar las piezas. Se instala con "pip install numpy"

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

    def comprobar_colision(self, piece):
        # Comprueba si la pieza colisiona con el tablero o con otra pieza
        for i in range(len(piece.blocks)):
            for j in range(len(piece.blocks[i])):
                if piece.blocks[i][j] != 0:
                    if piece.y + i >= self.height or self.grid[piece.y + i][piece.x + j] != 0:
                        return True
        return False
    
    def draw(self, screen):
        # Dibuja la grilla del juego
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, constantes.GRAY, (j * constantes.BLOCK_SIZE, i * constantes.BLOCK_SIZE, constantes.BLOCK_SIZE, constantes.BLOCK_SIZE), 1)

    def añadir_piezas(self, piece):
        # Añade la pieza al tablero
        for i in range(len(piece.blocks)):
            for j in range(len(piece.blocks[i])):
                if piece.blocks[i][j] != 0:
                    self.grid[piece.y + i][piece.x + j] = piece.color

    def check_filas(self):
        # Comprueba si hay filas llenas y las elimina
        filas = []
        for i in range(self.height):
            if all(self.grid[i]):
                filas.append(i)
        if filas:
            for row in reversed(filas):
                self.grid.pop(row)
                self.grid.insert(0, [0] * self.width)

        # Actualiza la puntuación y el nivel
        self.score += len(filas) * 10
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
        # return any(self.grid[0]) # Otra forma de hacerlo 

    def draw(self, screen, font):
        # Dibuja el tablero y la información del juego en pantalla
        self.draw_grid(screen)
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] != 0:
                    pygame.draw.rect(screen, self.grid[i][j], (j * constantes.BLOCK_SIZE, i * constantes.BLOCK_SIZE, constantes.BLOCK_SIZE, constantes.BLOCK_SIZE))
        score_text = font.render("Score: {}".format(self.score), 1, (255, 255, 255))
        level_text = font.render("Level: {}".format(self.level), 1, (255, 255, 255))
        screen.blit(score_text, (constantes.BOARD_WIDTH * constantes.BLOCK_SIZE + 10, 50))
        screen.blit(level_text, (constantes.BOARD_WIDTH * constantes.BLOCK_SIZE + 10, 100))

class Game:
    def __init__(self):
        self.board = Board(constantes.BOARD_WIDTH, constantes.HEIGHT)
        self.pieces = None
        self.next_pieces = None
        self.run = True
        self.gameover = False
        self.clock = pygame.time.Clock()
        self.fall_time = 0
        self.fall_speed = 500
        self.font = pygame.font.SysFont("Times New Roman", 50)

    def update_display(self):
    # Actualiza el display con la información del tablero y la pieza actual
        self.screen.fill((0, 0, 0))
        self.board.draw(self.screen, self.font)
        self.current_piece.draw(self.screen, self.font)
        pygame.display.update()

    def get_current_piece(self):
        # Devuelve la pieza actual
        return self.current_piece

    def get_next_piece(self):
        # Devuelve la siguiente pieza
        return self.next_piece

    def generar_piezas(self):
        # Genera una pieza aleatoria
        return Piece(5, 0, random.choice(constantes.PIECES)) # Duda sobre esta funcion

    def check_input(self):
        keys: list = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.get_current_piece().move_left()
            if self.board.comprobar_colision(self.get_current_piece()):
                self.get_current_piece().move_right()
        if keys[pygame.K_RIGHT]:
            self.get_current_piece().move_right()
            if self.board.comprobar_colision(self.get_current_piece()):
                self.get_current_piece().move_left()
        if keys[pygame.K_DOWN]:
            self.get_current_piece().move_down()
            if self.board.comprobar_colision(self.get_current_piece()):
                self.get_current_piece().move_up()
        if keys[pygame.K_UP]:
            self.get_current_piece().rotate()
            if self.board.comprobar_colision(self.get_current_piece()):
                self.get_current_piece().rotate(False)
        if keys[pygame.K_SPACE]:
            self.get_current_piece().move_down()
            while not self.board.comprobar_colision(self.get_current_piece()):
                self.get_current_piece().move_down()
            self.get_current_piece().move_up()
    
    def update(self):
        # Actualiza el juego y la pieza actual 
        self.fall_time += self.clock.get_rawtime()
        self.clock.tick()
        if self.fall_time / 1000 >= self.fall_speed / 1000:
            self.fall_time = 0
            self.get_current_piece().move_down()
            if self.board.comprobar_colision(self.get_current_piece()):
                self.get_current_piece().move_up()
                self.board.añadir_piezas(self.get_current_piece())
                self.board.check_filas()
                if self.board.comprobar_gameover():
                    self.gameover = True
                self.current_piece = self.next_piece
                self.next_piece = self.pieces.generar_piezas()
    
    def run(self):
        # Bucle principal del juego
        while self.run:
            if self.gameover:
                self.run = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
            self.check_input()
            self.update()
            self.update_display()
        pygame.quit()