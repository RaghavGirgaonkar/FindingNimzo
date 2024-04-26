import chess
from search import alpha_beta_pruning_search

search_depth = 4

def play():
    board = chess.Board()
    move_number = 1
    while not board.is_game_over():
        print('----------------')
        print('Move', move_number)
        print(board)
        if board.turn:
            move = input('Enter move: ')
            try:
                board.push_san(move)
            except:
                print('Invalid move!')
                continue
        else:
            print('Computer is thinking...')
            _, move = alpha_beta_pruning_search(board, search_depth, -9999, 9999, True)
            board.push(move)
            print('Computer moves:', move)
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