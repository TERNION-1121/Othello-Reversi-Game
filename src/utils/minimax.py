from utils.board import Board, np

def minimax(position: Board, depth: int, isMaximizingPlayer: bool) -> int:
    if depth == 0 or position.check_game_over() is True:
        return position.evaluate_board()
    
    if isMaximizingPlayer:
        maxEval = float('-inf')
        legal_moves = position.all_legal_moves(Board.BLACK)
        for row, col in legal_moves:
            if position.board[row, col] == Board.EMPTY:
                position.board[row, col] = Board.BLACK

                eval = minimax(position, depth - 1, False)
                maxEval = max(maxEval, eval)

                position.board[row, col] = Board.EMPTY
        return maxEval

    # else minimizing player's turn
    minEval = float('+inf')
    legal_moves = position.all_legal_moves(Board.WHITE)
    for row, col in legal_moves:
        if position.board[row, col] == Board.EMPTY:
            position.board[row, col] = Board.WHITE

            eval = minimax(position, depth - 1, True)
            minEval = min(minEval, eval)

            position.board[row, col] = Board.EMPTY
    return minEval

def find_best_move(position: Board) -> tuple[int, int]:
    bestMove = (20, 20)
    bestEval = float('+inf')

    legal_moves = position.all_legal_moves(Board.WHITE)
    for row, col in legal_moves:
        if position.board[row, col] == Board.EMPTY:
            position.board[row, col] = Board.WHITE

            currentEval = minimax(position, 2, False)

            position.board[row, col] = Board.EMPTY

            if currentEval < bestEval:
                bestMove = (row, col)
                bestEval = currentEval
    print(bestEval)
    return bestMove