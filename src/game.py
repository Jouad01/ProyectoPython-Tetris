import pygame
import random
from board import *

# con esta clase se crea las piezas que usaran otras funciones
# shape es la forma de la pieza, x y las coordenadas
class Piece(object):  
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

# crea una array llamada grid de 20 filas y 10 columnas que representa el tablero del Tetris
# si la coordenada de la celda está en el diccionario locked_pos, se asigna el color de la celda desde el diccionario 
# de lo contrario, se asigna el color negro a la celda.
def create_grid(locked_pos={}): 
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
    # bucle que recorre la matriz de la pieza y devuelve una lista de coordenadas de las celdas que no son cero
    # para asi poder dibujar la pieza en el tablero
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions

# devuelve True si la pieza puede colocarse en el tablero en su posición actual, de lo contrario devuelve False.
def valid_space(shape, grid):
    # recibe la pieza y el tablero para comprobar si la pieza puede colocarse en el tablero
    pos_okay = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    # si la celda tiene el color negro (0,0,0) se añade a la lista pos_okay
    pos_okay = [j for sub in pos_okay for j in sub]

    # convertimos la forma de la pieza en una lista de coordenadas
    transform = convert_shape_format(shape)

    for pos in transform:
        if pos not in pos_okay:
            if pos[1] > -1:
                return False
    return True

# comprueba si alguna pieza ha llegado a la parte superior del tablero
def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

# funcion que devuelve una pieza aleatoria
def get_shape():
    return Piece(5, 0, random.choice(shapes))

# uso de pygame para dibujar el tablero
def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("Times New Roman", size, bold=True)
    label = font.render(text, 1, color)
    # calculo de la posicion del texto en el centro de la pantalla. Surface.blit() dibuja la imagen en la superficie
    surface.blit(label, (LEFT_X + TETRIS_WIDTH /2 - (label.get_width()/2), LEFT_Y + TETRIS_HEIGHT/2 - label.get_height()/2))


def draw_grid(surface, grid):
    sx = LEFT_X
    sy = LEFT_Y

    for i in range(len(grid)):
        # fondo del tablero en color negro
        # dibuja las lineas verticales y horizontales del tablero
        pygame.draw.line(surface, (128, 128 ,128), (sx, sy + i*BLOCK_SIZE), (sx+TETRIS_WIDTH, sy+ i*BLOCK_SIZE))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j*BLOCK_SIZE, sy),(sx + j*BLOCK_SIZE, sy + TETRIS_HEIGHT))

# funcion para eliminar las filas completas
def clear_rows(grid, locked):
    # locked es un diccionario que almacena las piezas y grid lista de listas que representa el tablero
    # inicializamos un contador de filas completas
    # recorremos las filas del tablero desde abajo hacia arriba
    cont = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        # si no hay ningun bloque vacio en la fila aumentamos el contador de filas completas
        if (0,0,0) not in row:
            cont += 1
        # guardamos el indice de la fila completa
            indice = i
            for j in range(len(row)):
                try:
                # eliminamos la posicion de la fila completa del diccionario de posiciones bloqueadas
                    del locked[(j,i)]
                except:
                    continue
    if cont > 0:
        # recorremos las posiciones bloqueadas ordenadas por coordenada Y 
        # si hay alguna fila que se encuentre por encima de la fila completa
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < indice:
            # movemos la posicion hacia abajo en el numero de filas completas
                newKey = (x, y + cont)
                locked[newKey] = locked.pop(key)
    return cont

# uso de pygame, funcion que dibuja la pieza en el tablero
def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('Times New Roman', 30)
    label = font.render('Siguiente pieza', 1, (255,255,255))

    sx = LEFT_X + TETRIS_WIDTH + 50
    sy = LEFT_Y + TETRIS_HEIGHT/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            # si la columna es 0, dibuja el cuadrado de la pieza
            if column == '0':
                # calculo de la posicion del cuadrado
                pygame.draw.rect(surface, shape.color, (sx + j*BLOCK_SIZE, sy + i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

    surface.blit(label, (sx + 10, sy - 30))


# Para guardar la puntuacion en un fichero 
def update_score(actual_score):
    try:
        score = max_score()
    except Exception as e:
        print("Error: ", e)
        score = None
    
    try:
        with open('utilities/record.txt', 'w') as f:
            if score and int(score) > actual_score:
                f.write(str(score))
            else:
                f.write(str(actual_score))
    except Exception as e:
        print("Error: ", e)

def max_score():
    try:
        with open('utilities/record.txt', 'r') as f:
            lines = f.readlines()
            score = lines[0].strip()
    except Exception as e:
        print("Error: ", e)
        score = None
    return score



# uso de pygame, funcion que dibuja la ventana
# puntuacion, fondo, tamaño, color, etc
def draw_window(surface, grid, score=0, last_score = 0):
    surface.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('IMPACT', 60)
    label = font.render('Tetris', 1, (255, 255, 255))

    # calculo de la posicion del texto
    surface.blit(label, (LEFT_X + TETRIS_WIDTH / 2 - (label.get_width() / 2), 30))

    # puntuacion actual
    font = pygame.font.SysFont('Times New Roman', 30)
    label = font.render('Puntos: ' + str(score), 1, (255,255,255))

    sx = LEFT_X + TETRIS_WIDTH + 50
    sy = LEFT_Y + TETRIS_HEIGHT/2 - 100

    surface.blit(label, (sx + 20, sy + 160))
    # puntuacion maxima
    label = font.render('Record: ' + last_score, 1, (255,255,255))

    sx = LEFT_X - 200
    sy = LEFT_Y + 200


    surface.blit(label, (sx + 20, sy + 160))

    # este bucle recorre el tablero y dibuja los cuadrados
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # para cada posicion del tablero, si no es 0, dibuja el cuadrado. 0 es el color
            pygame.draw.rect(surface, grid[i][j], (LEFT_X + j*BLOCK_SIZE, LEFT_Y + i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    # color bordes
    pygame.draw.rect(surface, (255, 255, 255), (LEFT_X, LEFT_Y, TETRIS_WIDTH, TETRIS_HEIGHT), 5)

    draw_grid(surface, grid)