import chess
from hyperparameters import *


def evaluate_board(board):
    white_pieces = {'p': 0, 'n': 0, 'b': 0, 'r': 0, 'q': 0, 'k': 0}
    black_pieces = {'p': 0, 'n': 0, 'b': 0, 'r': 0, 'q': 0, 'k': 0}
    PIECE_MAP = board.piece_map();
    bonus_score = 0
    material_score = 0
    mobility_score = 0

    if board.is_checkmate():
        return -GAME_LOSS_SCORE if board.turn else GAME_LOSS_SCORE
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0
    
    for key in PIECE_MAP.keys():
        piece = PIECE_MAP[key].symbol()
        match piece:
            case 'P':
                bonus_score += PAWN_BONUS_TABLE_WHITE[63-key]
                white_pieces['p'] += 1
            case 'p':
                bonus_score += PAWN_BONUS_TABLE_BLACK[63-key]
                black_pieces['p'] += 1
            case 'N':
                bonus_score += KNIGHT_BONUS_TABLE_WHITE[63-key]
                white_pieces['n'] += 1
            case 'n':
                bonus_score += KNIGHT_BONUS_TABLE_BLACK[63-key]
                black_pieces['n'] += 1
            case 'B':
                bonus_score += BISHOP_BONUS_TABLE_WHITE[63-key]
                white_pieces['b'] += 1
            case 'b':
                bonus_score += BISHOP_BONUS_TABLE_BLACK[63-key]
                black_pieces['b'] += 1
            case 'R':
                bonus_score += ROOK_BONUS_TABLE_WHITE[63-key]
                white_pieces['r'] += 1
            case 'r':
                bonus_score += ROOK_BONUS_TABLE_BLACK[63-key]
                black_pieces['r'] += 1
            case 'Q':
                bonus_score += QUEEN_BONUS_TABLE_WHITE[63-key]
                white_pieces['q'] += 1
            case 'q':
                bonus_score += QUEEN_BONUS_TABLE_BLACK[63-key]
                black_pieces['q'] += 1
            case 'K':
                bonus_score += KING_BONUS_TABLE_WHITE[63-key]
                white_pieces['k'] += 1
            case 'k':
                bonus_score += KING_BONUS_TABLE_BLACK[63-key]
                black_pieces['k'] += 1
    

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
    
    return material_score + 0.1 * mobility_score + 0.08 * bonus_score

if __name__ == '__main__':
    board = chess.Board('rnbqkbnr/ppppp1pp/8/5p2/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2')
    eval = evaluate_board(board)
    print(eval)