import pygame
import numpy as np

# Definir dimensiones de la pantalla
WIDTH, HEIGHT = 800, 800
# Definir tamaño de celda
CELL_SIZE = 10
# Calcular número de celdas en cada dirección
N_ROWS, N_COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

# Inicializar la ventana de Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def create_board():
    return np.zeros((N_ROWS, N_COLS))


def draw_board(board):
    for i in range(N_ROWS):
        for j in range(N_COLS):
            if board[i][j] == 1:
                pygame.draw.rect(screen, (255, 255, 255),
                                (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(
                    screen, (0, 0, 0), (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()


def next_board_state(board):
    new_board = np.zeros((N_ROWS, N_COLS))
    for i in range(1, N_ROWS-1):
        for j in range(1, N_COLS-1):
            neighbors = np.sum(board[i-1:i+2, j-1:j+2]) - board[i][j]
            if board[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                new_board[i][j] = 0
            elif board[i][j] == 0 and neighbors == 3:
                new_board[i][j] = 1
            else:
                new_board[i][j] = board[i][j]
    return new_board


def handle_mouse_click(pos, board):
    row, col = pos[1] // CELL_SIZE, pos[0] // CELL_SIZE
    board[row][col] = 1 - board[row][col]


def main():
    board = create_board()
    editing = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if editing:
                    handle_mouse_click(pygame.mouse.get_pos(), board)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Agregar verificación para borrar todos los cuadros blancos y activar el modo de edición
                    board = create_board()
                    editing = True
                elif event.key == pygame.K_SPACE:
                    editing = not editing

        if not editing:
            board = next_board_state(board)
        draw_board(board)
        pygame.time.wait(100)


if __name__ == '__main__':
    main()
