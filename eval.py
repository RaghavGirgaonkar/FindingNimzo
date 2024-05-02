import chess
from hyperparameters import *


def evaluate_board(board):
    BONUS_TABLES = {'p': PAWN_BONUS_TABLE_BLACK, 
                    'n': KNIGHT_BONUS_TABLE_BLACK, 
                    'b': BISHOP_BONUS_TABLE_BLACK, 
                    'r': ROOK_BONUS_TABLE_BLACK, 
                    'q': QUEEN_BONUS_TABLE_BLACK, 
                    'k': KING_BONUS_TABLE_BLACK,
                    'P': PAWN_BONUS_TABLE_WHITE,
                    'N': KNIGHT_BONUS_TABLE_WHITE,
                    'B': BISHOP_BONUS_TABLE_WHITE,
                    'R': ROOK_BONUS_TABLE_WHITE,
                    'Q': QUEEN_BONUS_TABLE_WHITE,
                    'K': KING_BONUS_TABLE_WHITE}
    
    PIECE_MAP = board.piece_map()
    bonus_score = 0
    material_score = 0
    mobility_score = 0

    if board.is_checkmate():
        return -GAME_LOSS_SCORE if board.turn else GAME_LOSS_SCORE
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0

    for square, piece in PIECE_MAP.items():
        piece_symbol = piece.symbol()
        
        color_multiplier = 1 if piece.color == chess.WHITE else -1
        bonus_score += color_multiplier * BONUS_TABLES[piece_symbol][63-square]
        material_score += color_multiplier * PIECE_VALUES[piece_symbol]
        
    mobility_score = calculate_mobility(board)

    eval_score = material_score + 0.1 * mobility_score + 0.3 * bonus_score

    return eval_score


def calculate_mobility(board):
    legal_moves = list(board.legal_moves)
    mobility_score_white = len(legal_moves)
    board.push(chess.Move.null())  # Switch turn
    legal_moves = list(board.legal_moves)
    mobility_score_black = len(legal_moves)
    board.pop()  # Restore board state
    return mobility_score_white - mobility_score_black


if __name__ == '__main__':
    board = chess.Board('r3k2r/ppp2ppp/2n5/3qP3/6b1/2P3P1/PPP4P/R4RK1 b kq - 1 15')
    eval_score = evaluate_board(board)
    print(eval_score)
