from random import randint
from BoardClasses import Move
from BoardClasses import Board
#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.
class StudentAI():

    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2
    def get_move(self,move):
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        index = randint(0,len(moves)-1)
        inner_index =  randint(0,len(moves[index])-1)
        move = moves[index][inner_index]
        self.board.make_move(move,self.color)
        return move

    def board_score(self):
        w_points = 0; b_points = 0;
        for c in range(self.col):
            for r in range(self.row):
                if self.board[c][r].get_color() == 'W':
                    if self.board[c][r].is_king == True:
                        w_points += 1.2;
                    else:
                        w_points += 1;
                elif self.board[c][r].get_color() == 'B':
                    if self.board[c][r].is_king == True:
                        b_points += 1.2;
                    else:
                        b_points += 1;
                else:
                    pass;
        return w_points - b_points;
