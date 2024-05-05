from multiprocessing import Pool
from eval import evaluate_board
from hyperparameters import *
from moveOrdering import *
import multiprocessing
import chess.polyglot
import argparse
import chess
import time

def minimax_search(board, depth, is_maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None
    
    if is_maximizing:
        max_eval = -9999
        best_move = None

        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax_search(board, depth - 1, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move

        return max_eval, best_move
    else:
        min_eval = 9999
        best_move = None

        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax_search(board, depth - 1, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move

        return min_eval, best_move
    
def quiescence_search(board, alpha, beta, turnMultiplier):
    '''
    After reaching depth limit, Search all capture moves until a quiet position is found.
    '''
    # #Get all capture moves
    capture_moves = []
    for move in board.legal_moves:
        if board.is_capture(move):
            capture_moves.append(move)

    stand_pat = turnMultiplier * evaluate_board(board)

    if stand_pat >= beta:
        return beta, None
    if alpha < stand_pat:
        alpha = stand_pat

    maxScore = -GAME_LOSS_SCORE
    best_move = None

    for move in capture_moves:
        board.push(move)
        score, _ = quiescence_search(board, -beta, -alpha, -turnMultiplier)
        score *= -1
        board.pop()

        if score >= beta:
            return beta, move
        if score > maxScore:
            maxScore = score
            best_move = move
        if score > alpha:
            alpha = score

    

    return maxScore, best_move

def alpha_beta_pruning_search(board, transposition_table, depth, alpha, beta, is_maximizing):
    '''
    Basic alpha-beta pruning search function
    '''
    if depth == 0 or board.is_game_over():
        hash = chess.polyglot.zobrist_hash(board)
        if hash in transposition_table:
            return transposition_table[hash], None
        else:
            eval = evaluate_board(board)
            transposition_table[hash] = eval
            return eval, None

    # if depth == 0:
    #     eval, best_move = quiescence_search(board, alpha, beta, is_maximizing)
    #     return eval, best_move

    if is_maximizing:
        max_eval = -9999
        best_move = None

        for move in board.legal_moves:
            board.push(move)
            eval, _ = alpha_beta_pruning_search(board, transposition_table, depth - 1, alpha, beta, False)
            board.pop()
            if eval >= max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return max_eval, best_move
    else:
        min_eval = 9999
        best_move = None

        for move in board.legal_moves:
            board.push(move)
            eval, _ = alpha_beta_pruning_search(board, transposition_table, depth - 1, alpha, beta, True)
            board.pop()
            if eval <= min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break

        return min_eval, best_move

def alpha_beta_negamax_search(board, transposition_table, depth, alpha, beta, turnMultiplier):
    '''
    A cleaner implementation of an alpha beta pruning minimax search
    '''
    if depth == 0 or board.is_game_over():
        hash = chess.polyglot.zobrist_hash(board)
        if hash in transposition_table:
            return transposition_table[hash], None
        else:
            eval = turnMultiplier*evaluate_board(board)
            transposition_table[hash] = eval
            return eval, None

    # if board.is_game_over():
    #     hash = chess.polyglot.zobrist_hash(board)
    #     eval = turnMultiplier*evaluate_board(board)
    #     transposition_table[hash] = eval
    #     return eval, None

    # if depth == 0:
    #     hash = chess.polyglot.zobrist_hash(board)
    #     if hash not in transposition_table:
    #         eval = turnMultiplier*evaluate_board(board)
    #         transposition_table[hash] = eval
    #         eval, best_move = quiescence_search(board, alpha, beta, turnMultiplier) 
            

    # if depth <= 1:  # Apply quiescence search at lower depths
    #     eval, best_move = quiescence_search(board, alpha, beta, turnMultiplier)
    #     return eval, best_move

    maxScore = -GAME_LOSS_SCORE
    best_move = None  # Initialize best_move 
    all_legal_moves = board.legal_moves
    sorted_moves = order_moves(board,all_legal_moves,None)

    for move in sorted_moves:
        board.push(move)
        eval, _ = alpha_beta_negamax_search(board, transposition_table, depth -1, -beta, -alpha, -turnMultiplier)
        eval *= -1
        board.pop()
        if eval >= maxScore:
            maxScore = eval
            best_move = move
            #Pruning
        if maxScore > alpha:
            alpha = maxScore
        if alpha > beta:
            break

    return maxScore, best_move

def iterative_deepening_search(board, transposition_table, max_depth, turnMultiplier):
    best_move = None
    for depth in range(1, max_depth):
        eval, best_move = alpha_beta_negamax_search(board, transposition_table, depth, -9999, 9999, turnMultiplier)

    return eval, best_move


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Chess AI')
    parser.add_argument('depth', type=int, help='Search depth')
    args = parser.parse_args()
    search_depth = args.depth

    board = chess.Board('r3k2r/ppp2ppp/2n5/3qP3/6b1/2P3P1/PPP4P/R4RK1 b kq - 1 15')

    start_time = time.time()
    transposition_table = {}

    eval, best_move = iterative_deepening_search(board, transposition_table, search_depth, 1)
    end_time = time.time()
    print("Number of keys in transposition table: ", len(transposition_table))
    
    print(eval, best_move)
    print('Iterative Deepening Search Time taken {}, with depth {}'.format(end_time - start_time, search_depth))