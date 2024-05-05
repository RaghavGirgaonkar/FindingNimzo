#All MACROS

NUM_WORKERS = 8

PIECE_VALUES = {'p': 100, 'n': 305, 'b': 332, 'r': 565, 'q': 950, 'k': 1000000, 
                'P': 100, 'N': 305, 'B': 332, 'R': 565, 'Q': 950, 'K': 1000000}

GAME_LOSS_SCORE = 1e6
ENDGAME_THRESHOLD = 2 * PIECE_VALUES['R'] + 2 * PIECE_VALUES['B'] + 2 * PIECE_VALUES['N'] + 2 * PIECE_VALUES['Q']

PAWN_BONUS_TABLE_WHITE = [0,  0,  0,  0,  0,  0,  0,  0, 
                          50, 50, 50, 50, 50, 50, 50, 50,
                          10, 10, 20, 30, 30, 20, 10, 10,
                           5,  5, 10, 25, 25, 10,  5,  5,
                           0,  0,  0, 20, 20,  0,  0,  0,
                           5, -5,-10,  0,  0,-10, -5,  5,
                           5, 10, 10,-20,-20, 10, 10,  5,
                           0,  0,  0,  0,  0,  0,  0,  0]

PAWN_BONUS_TABLE_BLACK = [-1*x for x in PAWN_BONUS_TABLE_WHITE[::-1]]

PAWN_BONUS_TABLE_WHITE_END = [0,   0,   0,   0,   0,   0,   0,   0,
			                  80,  80,  80,  80,  80,  80,  80,  80,
			                  50,  50,  50,  50,  50,  50,  50,  50,
			                  30,  30,  30,  30,  30,  30,  30,  30,
			                  20,  20,  20,  20,  20,  20,  20,  20,
			                  10,  10,  10,  10,  10,  10,  10,  10,
			                  10,  10,  10,  10,  10,  10,  10,  10,
			                  0,   0,   0,   0,   0,   0,   0,   0]

PAWN_BONUS_TABLE_BLACK_END = [-1*x for x in PAWN_BONUS_TABLE_WHITE_END[::-1]]

KNIGHT_BONUS_TABLE_WHITE = [-50,-40,-30,-30,-30,-30,-40,-50,
                            -40,-20,  0,  0,  0,  0,-20,-40,
                            -30,  0, 10, 15, 15, 10,  0,-30,
                            -30,  5, 15, 20, 20, 15,  5,-30,
                            -30,  0, 15, 20, 20, 15,  0,-30,
                            -30,  5, 10, 15, 15, 10,  5,-30,
                            -40,-20,  0,  5,  5,  0,-20,-40,
                            -50,-40,-30,-30,-30,-30,-40,-50]
KNIGHT_BONUS_TABLE_BLACK = [-1*x for x in KNIGHT_BONUS_TABLE_WHITE[::-1]]

BISHOP_BONUS_TABLE_WHITE = [-20,-10,-10,-10,-10,-10,-10,-20,
                            -10,  0,  0,  0,  0,  0,  0,-10,
                            -10,  0,  5, 10, 10,  5,  0,-10,
                            -10,  5,  5, 10, 10,  5,  5,-10,
                             10,  0, 10, 10, 10, 10,  0,-10,
                            -10, 10, 10, 10, 10, 10, 10,-10,
                            -10,  5,  0,  0,  0,  0,  5,-10,
                            -20,-10,-10,-10,-10,-10,-10,-20]
BISHOP_BONUS_TABLE_BLACK = [-1*x for x in BISHOP_BONUS_TABLE_WHITE[::-1]]

ROOK_BONUS_TABLE_WHITE = [0,  0,  0,  0,  0,  0,  0,  0,
                          5, 10, 10, 10, 10, 10, 10,  5,
                         -5,  0,  0,  0,  0,  0,  0, -5,
                         -5,  0,  0,  0,  0,  0,  0, -5,
                         -5,  0,  0,  0,  0,  0,  0, -5,
                         -5,  0,  0,  0,  0,  0,  0, -5,
                         -5,  0,  0,  0,  0,  0,  0, -5,
                          0,  0,  0,  5,  5,  0,  0,  0]
ROOK_BONUS_TABLE_BLACK = [-1*x for x in ROOK_BONUS_TABLE_WHITE[::-1]]

QUEEN_BONUS_TABLE_WHITE = [-20,-10,-10, -5, -5,-10,-10,-20,
                           -10,  0,  0,  0,  0,  0,  0,-10,
                           -10,  0,  5,  5,  5,  5,  0,-10,
                           -5,  0,  5,  5,  5,  5,  0, -5,
                            0,  0,  5,  5,  5,  5,  0, -5,
                           -10,  5,  5,  5,  5,  5,  0,-10,
                           -10,  0,  5,  0,  0,  0,  0,-10,
                           -20,-10,-10, -5, -5,-10,-10,-20]
QUEEN_BONUS_TABLE_BLACK = [-1*x for x in QUEEN_BONUS_TABLE_WHITE[::-1]]


KING_BONUS_TABLE_WHITE = [-30,-40,-40,-50,-50,-40,-40,-30,
                          -30,-40,-40,-50,-50,-40,-40,-30,
                          -30,-40,-40,-50,-50,-40,-40,-30,
                          -30,-40,-40,-50,-50,-40,-40,-30,
                          -20,-30,-30,-40,-40,-30,-30,-20,
                          -10,-20,-20,-20,-20,-20,-20,-10,
                           20, 20,  0,  0,  0,  0, 20, 20,
                           20, 30, 10,  0,  0, 10, 30, 20]
KING_BONUS_TABLE_BLACK = [-1*x for x in KING_BONUS_TABLE_WHITE[::-1]]


KING_BONUS_TABLE_WHITE_END = [-20, -10, -10, -10, -10, -10, -10, -20,
			                  -5,   0,   5,   5,   5,   5,   0,  -5,
			                  -10, -5,   20,  30,  30,  20,  -5, -10,
			                  -15, -10,  35,  45,  45,  35, -10, -15,
			                  -20, -15,  30,  40,  40,  30, -15, -20,
			                  -25, -20,  20,  25,  25,  20, -20, -25,
			                  -30, -25,   0,   0,   0,   0, -25, -30,
			                  -50, -30, -30, -30, -30, -30, -30, -50]

KING_BONUS_TABLE_BLACK_END = [-1*x for x in KING_BONUS_TABLE_WHITE_END[::-1]]

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
    
BONUS_TABLES_END = {'p': PAWN_BONUS_TABLE_BLACK_END, 
                    'n': KNIGHT_BONUS_TABLE_BLACK, 
                    'b': BISHOP_BONUS_TABLE_BLACK, 
                    'r': ROOK_BONUS_TABLE_BLACK, 
                    'q': QUEEN_BONUS_TABLE_BLACK, 
                    'k': KING_BONUS_TABLE_BLACK_END,
                    'P': PAWN_BONUS_TABLE_WHITE_END,
                    'N': KNIGHT_BONUS_TABLE_WHITE,
                    'B': BISHOP_BONUS_TABLE_WHITE,
                    'R': ROOK_BONUS_TABLE_WHITE,
                    'Q': QUEEN_BONUS_TABLE_WHITE,
                    'K': KING_BONUS_TABLE_WHITE_END}