import pygame

import Logica.constantes as constantes
import Logica.game as game


def main():
    pygame.init()
    pygame.display.set_caption("Tetris")
    screen = pygame.display.set_mode((constantes.BOARD_WIDTH * constantes.BLOCK_SIZE, constantes.BOARD_HEIGHT * constantes.BLOCK_SIZE))
    game = game.Game(screen)
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()
