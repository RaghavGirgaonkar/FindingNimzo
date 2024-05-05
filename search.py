from eval import evaluate_board
from hyperparameters import *
from moveOrdering import *
import argparse
import chess
import chess.polyglot
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
    
def quiescence_search(board, alpha, beta, is_maximizing):
    '''
    After reaching depth limit, Search all capture moves until a quiet position is found.
    '''
    # #Get all capture moves
    capture_moves = []
    for move in board.legal_moves:
        if board.is_capture(move):
            capture_moves.append(move)
    return capture_moves

    if is_maximizing:
        max_eval = -9999
        best_move = None

        for move in capture_moves:
            board.push(move)
            eval, _ = quiescence_search(board, alpha, beta, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return max_eval, best_move
    else:
        min_eval = 9999
        best_move = None

        for move in capture_moves:
            board.push(move)
            eval, _ = quiescence_search(board, alpha, beta, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break

        return min_eval, best_move

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
            if eval > max_eval:
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
            if eval < min_eval:
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

    # if depth == 0:
    #     eval, best_move = quiescence_search(board, alpha, beta, is_maximizing)
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
        if eval > maxScore:
            maxScore = eval
            best_move = move
            #Pruning
        if maxScore > alpha:
            alpha = maxScore
        if alpha >= beta:
            break

    return maxScore, best_move

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Chess AI')
    parser.add_argument('depth', type=int, help='Search depth')
    args = parser.parse_args()
    search_depth = args.depth

    board = chess.Board('r3k2r/ppp2ppp/2n5/3qP3/6b1/2P3P1/PPP4P/R4RK1 b kq - 1 15')

    start_time = time.time()
    transposition_table = {}
    eval, best_move = alpha_beta_pruning_search(board, transposition_table, search_depth, -9999, 9999, True)
    # eval, best_move = alpha_beta_negamax_search(board, transposition_table, search_depth, -9999, 9999, 1)
    end_time = time.time()
    print("Number of keys in transposition table: ", len(transposition_table))
    
    print(eval, best_move)
    print('Time taken {}, with depth {}'.format(end_time - start_time, search_depth))
    start_time = time.time()
    transposition_table = {}
    # eval, best_move = alpha_beta_pruning_search(board, transposition_table, search_depth, -9999, 9999, True)
    eval, best_move = alpha_beta_negamax_search(board, transposition_table, search_depth, -9999, 9999, 1)
    end_time = time.time()
    print("Number of keys in transposition table: ", len(transposition_table))
    
    print(eval, best_move)
    print('Nega Max Search Time taken {}, with depth {}'.format(end_time - start_time, search_depth))