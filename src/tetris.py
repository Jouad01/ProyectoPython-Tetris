import pygame
import pymongo

from board import *
from game import *
# para poner sonido
from pygame.locals import *
from pygame import mixer

# Pedir al usuario que ingrese su nombre

print(" _______________________________________________ ")
print("|                    Tetris                     |")
print("|_______________________________________________|")
name = input("|   Usuario: ")
print("|_______________________________________________|")
pygame.font.init()


def main(win): 
    last_score = max_score()
    # diccionario para guardar las posiciones de las piezas que ya han caido
    locked_positions = {}
    grid = create_grid(locked_positions)
    
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    # clock para controlar los fps
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0
    
    # Soundtrack
    mixer.init()
    # Para cargar el archivo de audio hay que estar en /ProyectoPython-Tetris/src/ 
    mixer.music.load('utilities/crystals.mp3')
    # -1 para que se repita
    mixer.music.play(-1)

    # Conectarse a la base de datos
    try:
        client = pymongo.MongoClient("mongodb+srv://m002-student:12345@sandbox01.2yg0wjn.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        db = client["Tetris"]
        puntuaciones = db["usuarios"]
        print("Conectado a la base de datos")
    except:
        print("Error al conectarse a la base de datos")


    while run:
        # variables fall_time y level_time para controlar el tiempo de caida de la pieza
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        # usamos clock.tick() para que el juego no vaya mas rapido de lo que queremos
        clock.tick()

        # Aumenta la velocidad de caida segun el tiempo
        if level_time/1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005
        
        # Control de tiempo de caida de la pieza
        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not(valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        # Si se cierra la ventana se detiene el juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            # Uso de pygame para teclas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.rotation -= 1
                if event.key == pygame.K_SPACE:
                    run = False
                    pygame.display.quit()
        
        # se le asigna la lista de posiciones de la pieza actual
        shape_pos = convert_shape_format(current_piece)

        # recorre la pieza y asigna el color 
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        # se recorre posiciones de la pieza y se agrega cada una de ellas al diccionario
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            # se suma 10 puntos por cada fila eliminada
            score += clear_rows(grid, locked_positions) * 10

        draw_window(win, grid, score, last_score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            # Insertar datos en la base de datos
            puntuaciones.insert_one({ "nombre": name, "puntuacion": score})
            draw_text_middle(win, 'GAME OVER', 80, (255,255,255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            update_score(score)
            # se actualiza el ultimo puntaje si es mas alto
            if score > last_score:
                last_score = score
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.display.quit()

def main_menu(win):  
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle(win, 'Pulsa cualquier tecla para empezar', 50, (255,255,255))
        pygame.display.update()
        # si se presiona cualquier tecla se inicia el juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)

    pygame.display.quit()


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tetris: El Jueguito')
main_menu(win)