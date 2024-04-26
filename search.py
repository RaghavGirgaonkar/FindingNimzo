from eval import evaluate_board
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
    
def alpha_beta_pruning_search(board, depth, alpha, beta, is_maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    if is_maximizing:
        max_eval = -9999
        best_move = None

        for move in board.legal_moves:
            board.push(move)
            eval, _ = alpha_beta_pruning_search(board, depth - 1, alpha, beta, False)
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
            eval, _ = alpha_beta_pruning_search(board, depth - 1, alpha, beta, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break

        return min_eval, best_move


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Chess AI')
    parser.add_argument('depth', type=int, help='Search depth')
    args = parser.parse_args()
    search_depth = args.depth

    board = chess.Board('5r2/4qp2/2n1p3/3p4/5kPN/3r3Q/7P/4R1K1 w - - 0 40')

    start_time = time.time()
    eval, best_move = alpha_beta_pruning_search(board, search_depth, -9999, 9999, True)
    end_time = time.time()

    print(eval, best_move)
    print('Time taken {}, with depth {}:'.format(end_time - start_time, search_depth))