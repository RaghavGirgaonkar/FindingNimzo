import chess
import chess.polyglot
import chess.svg
from search import *
from eval import *
import argparse
import pickle
import random

opening_book = chess.polyglot.open_reader('bookfish.bin')

def play(search_depth, color, transposition_table, verbose=0):

    board = chess.Board()
    save_board_svg(board, not color)
    move_number = 1
    while not board.is_game_over():
        print('----------------')
        print('Move', move_number)
        if verbose:
            print(board)
            position_eval = evaluate_board(board)
            print('Position Eval:', position_eval)

        if board.turn == color:
            
            book_moves = [entry.move for entry in opening_book.find_all(board)]
            if book_moves:
                print('Computer is in book...')
                move = random.choice(book_moves)
                board.push(move)
            else:
                print('Computer is thinking...')
                
                move_eval, move = iterative_deepening_search(board, transposition_table,search_depth,1 if color else -1)
                board.push(move)
                
            if verbose:
                position_eval = evaluate_board(board)
                print('Position Eval:', position_eval)
            print('Computer moves:', move)
                
            move_number += 1
        else:
            move = input('Enter move: ')
            if move == 'exit':
                break
            try:
                board.push_san(move)
                if verbose:
                    position_eval = evaluate_board(board)
                    print('Position Eval:', position_eval)
            except:
                print('Invalid move!')
                continue
        save_board_svg(board, not color)
   
    print('----------------')
    
    print(board)

    if board.is_checkmate():
        print('Checkmate!')
    elif board.is_stalemate():
        print('Stalemate!')
    elif board.is_insufficient_material():
        print('Insufficient material!')

def save_board_svg(board, color=chess.WHITE):
    # Generate the SVG image of the current board
    svg = chess.svg.board(board=board, orientation=color)

    # Write the SVG content to a file
    with open(f'board.svg', 'w') as f:
        f.write(svg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--depth', type=int, default=4, help='Search depth')
    parser.add_argument('--color', type=str, default='white', help='Computer color')
    parser.add_argument('--verbose', type=int, default=1, help='Verbose mode')
                        
    args = parser.parse_args()
    
    # load transposition table
    transposition_table = {}
    try:
        with open('transposition_table.pkl', 'rb') as f:
            transposition_table = pickle.load(f)
    except:
        pass

    if args.color == 'white':
        play(args.depth, chess.WHITE, transposition_table, args.verbose)
    elif args.color == 'black':
        play(args.depth, chess.BLACK, transposition_table, args.verbose)
    else:
        print('Invalid color!')
    
    # save transposition table
    # with open('transposition_table.pkl', 'wb') as f:
    #     pickle.dump(transposition_table, f)

