# Fichero que contendrá el tiempo de caida de piezas, el ancho y los colores

BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BLOCK_SIZE = 30


SPEED_MS = 500

COLOR = {
    "rojo": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255),
    "amarillo": (255, 255, 0),
    "morado": (255, 0, 255),
    "naranja": (255, 128, 0),
    # Añadir más
}

WINDOW_WIDTH = BOARD_WIDTH * BLOCK_SIZE
WINDOW_HEIGHT = BOARD_HEIGHT * BLOCK_SIZE

# Colores de los bloques
BLOCK_COLORS = [
    COLOR["rojo"],
    COLOR["verde"],
    COLOR["azul"],
    COLOR["amarillo"],
    COLOR["morado"],
    COLOR["naranja"],
]

# Formas de las piezas
I_PIECE = [
    [1, 1, 1, 1]
]

J_PIECE = [
    [1, 0, 0],
    [1, 1, 1]
]

L_PIECE = [
    [0, 0, 1],
    [1, 1, 1]
]

O_PIECE = [
    [1, 1],
    [1, 1]
]

S_PIECE = [
    [0, 1, 1],
    [1, 1, 0]
]

T_PIECE = [
    [0, 1, 0],
    [1, 1, 1]
]

Z_PIECE = [
    [1, 1, 0],
    [0, 1, 1]
]

# Conjunto de piezas
PIECES = [I_PIECE, J_PIECE, L_PIECE, O_PIECE, S_PIECE, T_PIECE, Z_PIECE]