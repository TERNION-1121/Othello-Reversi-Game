import pygame
from functions import *

# board initialisations
game_board = Board()

# pygame initialisations
pygame.init()

SCREEN_SIZE = 800
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Othello/Reversi")

bBoard = pygame.image.load("images/Othello_Black_Side_Board.png")
wBoard = pygame.image.load("images/Othello_White_Side_Board.png")
black_disc = pygame.image.load("images/Black_Disc.png")
white_disc = pygame.image.load("images/White_Disc.png")
ring = pygame.image.load("images/ring.png").convert()
pygame.Surface.set_alpha(ring, 30)


screen.blit(bBoard, (0,0))
pygame.display.flip()

running = True
turn = Board.BLACK
shown_moves = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for row in range(8):
        for col in range(8):
            if game_board.board[row, col] == Board.BLACK:
                x = 100 + 75 * col
                y = 100 + 75 * row
                screen.blit(black_disc, (x,y))
                pygame.display.flip()

            elif game_board.board[row, col] == Board.WHITE:
                x = 100 + 75 * col
                y = 100 + 75 * row
                screen.blit(white_disc, (x,y))
                pygame.display.flip()
    
    if turn == Board.BLACK and not shown_moves:
        possible_moves = list(game_board.all_legal_moves(Board.BLACK))
        for pos in possible_moves:
            r, c = pos
            screen.blit(ring, (100 + 75 * c, 100 + 75 * r))
            pygame.display.flip()
        shown_moves = True

pygame.quit()