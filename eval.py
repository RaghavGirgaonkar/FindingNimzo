import chess
from hyperparameters import *


def evaluate_board(board):
    white_pieces = {'p': 0, 'n': 0, 'b': 0, 'r': 0, 'q': 0, 'k': 0}
    black_pieces = {'p': 0, 'n': 0, 'b': 0, 'r': 0, 'q': 0, 'k': 0}
    PIECE_MAP = board.piece_map();

    if board.is_checkmate():
        return -GAME_LOSS_SCORE if board.turn else GAME_LOSS_SCORE
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0
    
    white_pieces['p'] = len(board.pieces(chess.PAWN, chess.WHITE))
    white_pieces['n'] = len(board.pieces(chess.KNIGHT, chess.WHITE))
    white_pieces['b'] = len(board.pieces(chess.BISHOP, chess.WHITE))
    white_pieces['r'] = len(board.pieces(chess.ROOK, chess.WHITE))
    white_pieces['q'] = len(board.pieces(chess.QUEEN, chess.WHITE))
    white_pieces['k'] = len(board.pieces(chess.KING, chess.WHITE))

    black_pieces['p'] = len(board.pieces(chess.PAWN, chess.BLACK))
    black_pieces['n'] = len(board.pieces(chess.KNIGHT, chess.BLACK))
    black_pieces['b'] = len(board.pieces(chess.BISHOP, chess.BLACK))
    black_pieces['r'] = len(board.pieces(chess.ROOK, chess.BLACK))
    black_pieces['q'] = len(board.pieces(chess.QUEEN, chess.BLACK))
    black_pieces['k'] = len(board.pieces(chess.KING, chess.BLACK))

    for key in PIECE_MAP.keys():
        piece = PIECE_MAP[key].symbol()
        match piece:
            case 'P':
            case 'p':
            case 'N':
            case 'n':
            case 'B':
            case 'b':
            case 'R':
            case 'r':
            case 'Q':
            case 'q':
            case 'K':
            case 'k':
    

    material_score = PIECE_VALUES['p'] * (white_pieces['p'] - black_pieces['p']) + \
                     PIECE_VALUES['n'] * (white_pieces['n'] - black_pieces['n']) + \
                     PIECE_VALUES['b'] * (white_pieces['b'] - black_pieces['b']) + \
                     PIECE_VALUES['r'] * (white_pieces['r'] - black_pieces['r']) + \
                     PIECE_VALUES['q'] * (white_pieces['q'] - black_pieces['q']) + \
                     PIECE_VALUES['k'] * (white_pieces['k'] - black_pieces['k'])
    
    turn = board.turn
    board.turn = True
    mobility_score = len(list(board.legal_moves))
    board.turn = False
    mobility_score -= len(list(board.legal_moves))
    board.turn = turn
    
    return material_score + 0.1 * mobility_score

if __name__ == '__main__':
    board = chess.Board('rnbqkbnr/ppppp1pp/8/5p2/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2')
    eval = evaluate_board(board)
    print(eval)