#This will have a function to order all possible legal moves so that the best moves are searched first
# in order to reduce search time.
import chess

# Define piece values
piece_values = {
    chess.QUEEN: 950,
    chess.ROOK: 565,
    chess.KNIGHT: 305,
    chess.BISHOP: 332,
    chess.PAWN: 100
}

# Define evaluation values
evaluation_values = {
    chess.QUEEN: 950,
    chess.ROOK: 565,
    chess.KNIGHT: 305,
    chess.BISHOP: 332,
    chess.PAWN: 100
}

# Penalty for moving piece to a square attacked by opponent pawn
square_controlled_by_opponent_pawn_penalty = 350

# Multiplier for captured piece value
captured_piece_value_multiplier = 10

def order_moves(board, moves, hash_move=None):
    move_scores = {}
    
    for move in moves:
        score = 0
        move_piece_type = board.piece_type_at(move.from_square)
        capture_piece_type = board.piece_type_at(move.to_square)
        flag = move.promotion
        
        if capture_piece_type != None:
            # Order moves to try capturing the most valuable opponent piece with least valuable of own pieces first
            # The captured_piece_value_multiplier is used to make even 'bad' captures like QxP rank above non-captures
            score = captured_piece_value_multiplier * piece_values.get(capture_piece_type, 0) - piece_values.get(move_piece_type, 0)
        
        if move_piece_type == chess.PAWN:
            if flag == chess.QUEEN:
                score += evaluation_values[chess.QUEEN]
            elif flag == chess.KNIGHT:
                score += evaluation_values[chess.KNIGHT]
            elif flag == chess.ROOK:
                score += evaluation_values[chess.ROOK]
            elif flag == chess.BISHOP:
                score += evaluation_values[chess.BISHOP]
        else:
            # Penalize moving piece to a square attacked by opponent pawn
            if board.is_attacked_by(chess.BLACK, move.to_square):
                score -= square_controlled_by_opponent_pawn_penalty
        
        if move == hash_move:
            score += 10000
        
        move_scores[move] = score
    
    # Sort the moves list based on scores
    sorted_moves = sorted(moves, key=lambda move: move_scores[move], reverse=True)
    
    return sorted_moves
