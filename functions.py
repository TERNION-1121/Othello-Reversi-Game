import numpy as np

class Board:
    def __init__(self) -> None:
        '''Initiliaze the Othello game board with a 8x8 numpy matrix'''
        self.board = np.array([0]*8, dtype = np.int8)   # initiliasing 1D array with the first row of 8 zeroes
        self.board = self.board[np.newaxis, : ]         # expanding 1D array to 2D array
        for _ in range(3):                              # increasing rows till 8
            self.board = np.concatenate((self.board, self.board), axis = 0)

        # initiliasing the centre squares
        self.board[3, 3] = self.board[4,4] = -1
        self.board[3, 4] = self.board[4,3] =  1

        self.black_disc_count = 2
        self.white_disc_count = 2

    def print_board(self):
        print(self.board)