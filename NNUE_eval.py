import chess
from hyperparameters import *
import torch

input_feature_size = 40960

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.white_input = torch.nn.Linear(input_feature_size, 256)
        self.black_input = torch.nn.Linear(input_feature_size, 256)
        self.hidden_1 = torch.nn.Linear(512, 32)
        self.hidden_2 = torch.nn.Linear(32, 32)
        self.output = torch.nn.Linear(32, 1)

    def forward(self, x):
        white = self.white_input(x[:, :input_feature_size])
        black = self.black_input(x[:, input_feature_size:])
        x = torch.cat((white, black), dim=1)
        x = torch.relu(self.hidden_1(x))
        x = torch.relu(self.hidden_2(x))
        x = self.output(x)
        return x
    
def get_features(board): 
    white_features = torch.zeros(input_feature_size)
    black_features = torch.zeros(input_feature_size)

    white_king = board.king(chess.WHITE)
    black_king = board.king(chess.BLACK)
    
    for square in chess.SQUARES:
        for piece in [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN]:
            for color in [chess.WHITE, chess.BLACK]:
                if board.piece_at(square) == chess.Piece(piece, color):
                    white_index = white_king * 640 + square * 10 + piece * 2 + color
                    black_index = black_king * 640 + square * 10 + piece * 2 + color
                    white_features[white_king] = 1
                    black_features[black_king] = 1
                    print(white_index, white_king, square, piece, color)
                    print(black_index, black_king, square, piece, color)

                    
    return torch.cat((white_features, black_features))
                
if __name__ == '__main__':
    board = chess.Board('4k3/8/8/1N4b1/8/8/4P3/4K3 w - - 0 1')
    features = get_features(board)

