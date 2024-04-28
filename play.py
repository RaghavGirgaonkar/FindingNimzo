import chess
from search import alpha_beta_pruning_search
from eval import *

search_depth = 4

def play():
    board = chess.Board()
    move_number = 1
    while not board.is_game_over():
        print('----------------')
        print('Move', move_number)
        print(board)
        position_eval = evaluate_board(board)
        print('Position Eval:', position_eval)
        if board.turn:
            move = input('Enter move: ')
            try:
                board.push_san(move)
                position_eval = evaluate_board(board)
                print('Position Eval:', position_eval)
            except:
                print('Invalid move!')
                continue
        else:
            print('Computer is thinking...')
            move_eval, move = alpha_beta_pruning_search(board, search_depth, -9999, 9999, False)
            board.push(move)
            position_eval = evaluate_board(board)
            print('Computer moves:', move)
            print('Position Eval:', position_eval)
            move_number += 1

    print('----------------')
    print(board)
    if board.is_checkmate():
        print('Checkmate!')
    elif board.is_stalemate():
        print('Stalemate!')
    elif board.is_insufficient_material():
        print('Insufficient material!')

if __name__ == '__main__':
    play()