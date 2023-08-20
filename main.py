import numpy as np
import pygame
from functions import *

# board initialisations
game_board = Board()

# pygame initialisations
pygame.init()

SCREEN_SIZE = 800
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
screen.fill((255,255,255))
bBoard = pygame.image.load("images/Othello_Black_Side_Board.png")
wBoard = pygame.image.load("images/Othello_White_Side_Board.png")
black_disc = pygame.image.load("images/Black_Disc.png")
white_disc = pygame.image.load("images/White_Disc.png")


screen.blit(bBoard, (0,0))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for row in range(8):
        for col in range(8):
            if game_board.board[row, col] == 1:
                x = 100 * col + 5
                y = 100 * row + 5
                # screen.blit(black_disc, (x,y))
                # pygame.display.flip()

            elif game_board.board[row, col] == -1:
                x = 100 * col + 5
                y = 100 * row + 5
                # screen.blit(white_disc, (x,y))
                # pygame.display.flip()

pygame.quit()