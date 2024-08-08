import pygame

SQUARE_SIZE = 50

def board_init(board):
    res = (board.width * SQUARE_SIZE, board.height * SQUARE_SIZE)
    screen = pygame.display.set_mode(res)
    return screen

def draw(screen, board):
    screen.fill("cadetblue")
    
    for i in range(len(board.tiles)):
        for j in range(len(board.tiles[0])):
            if board.tiles[i][j]:
                pygame.draw.rect(screen, "ivory3", [j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE])
    
    for white_knight in board.white_knights:
        pygame.draw.rect(screen, "antiquewhite1", [white_knight[1] * SQUARE_SIZE, white_knight[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE])

    for black_knight in board.black_knights:
        pygame.draw.rect(screen, "black", [black_knight[1] * SQUARE_SIZE, black_knight[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE])

    pygame.draw.rect(screen, "royalblue3", [board.player[1] * SQUARE_SIZE, board.player[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE])
