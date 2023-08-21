import pygame
from functions import *

# board initialisations
game_board = Board()

# pygame initialisations
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Othello/Reversi")

bBoard = pygame.image.load("images/Othello_Black_Side_Board.png")
wBoard = pygame.image.load("images/Othello_White_Side_Board.png")
black_disc = pygame.image.load("images/Black_Disc.png")
white_disc = pygame.image.load("images/White_Disc.png")

possibleBlackMove = pygame.image.load("images/Black_Disc.png")
possibleWhiteMove = pygame.image.load("images/White_Disc.png")
pygame.Surface.set_alpha(possibleBlackMove, 50)
pygame.Surface.set_alpha(possibleWhiteMove, 50)

screen.blit(bBoard, (0,0))
pygame.display.flip()

running = True
turn = Board.BLACK
shown_moves = False
possible_moves = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            mx -= 100
            my -= 100
            r = my // 75
            c = mx // 75
            if (r,c) in possible_moves:
                game_board.set_discs(r, c, turn)
                shown_moves = False
                possible_moves.remove((r,c))
                for pos in possible_moves:
                    row, col = pos
                    x = 100 + 75 * col
                    y = 100 + 75 * row
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x+1, y+1, 70, 70))
                turn *= -1
                
    # display all the dics present on the board
    for row in range(8):
        for col in range(8):
            if game_board.board[row, col] == Board.BLACK:
                x = 100 + 75 * col
                y = 100 + 75 * row
                screen.blit(black_disc, (x,y))

            elif game_board.board[row, col] == Board.WHITE:
                x = 100 + 75 * col
                y = 100 + 75 * row
                screen.blit(white_disc, (x,y))
    
    if turn == Board.BLACK:
        if not shown_moves:
            possible_moves = list(game_board.all_legal_moves(Board.BLACK))
            if possible_moves == []:
                pass
            for pos in possible_moves:
                r, c = pos
                screen.blit(possibleBlackMove, (100 + 75 * c, 100 + 75 * r))
            
            shown_moves = True

    elif turn == Board.WHITE:
        if not shown_moves:
            possible_moves = list(game_board.all_legal_moves(Board.WHITE))
            if possible_moves == []:
                pass
            for pos in possible_moves:
                r, c = pos
                screen.blit(possibleWhiteMove, (100 + 75 * c, 100 + 75 * r))
            
            shown_moves = True

    pygame.display.flip()

pygame.quit()