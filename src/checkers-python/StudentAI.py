from random import randint
from BoardClasses import Move
from BoardClasses import Board
#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.


class StudentAI():

    def __init__(self, col, row, p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col, row, p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1: 2, 2: 1}
        self.color = 2

    def get_move(self, move):
        if len(move) != 0:
            self.board.make_move(move, self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)  # list of moves

        #Initializing the best_move/score as the first possible move/score
        index = randint(0,len(moves)-1)
        inner_index =  randint(0,len(moves[index])-1)
        best_move = moves[index][inner_index]
        self.board.make_move(best_move, self.color)
        best_score = self.board_score()
        self.board.undo()

        for i in moves:
            for ii in i:

                #changing to new gamestate
                self.board.make_move(ii, self.color)

                #grabbing list of opponents moves
                opponents_moves = self.board.get_all_possible_moves(
                    self.opponent[self.color])

                #initializing the min_move/scre as the first possible move of the opponent
                index = randint(0,len(opponents_moves)-1)
                inner_index =  randint(0,len(opponents_moves[index])-1)
                min_move = opponents_moves[index][inner_index]
                self.board.make_move(min_move, self.opponent[self.color])
                min_score = self.board_score()
                self.board.undo()

                #itterate through opponents moves to find the min value
                for j in opponents_moves:
                    for jj in j:
                        self.board.make_move(jj,self.opponent[self.color])

                        # Find the min between min_move and j
                        if( min_score > self.board_score() ):
                            min_score = self.board_score
                            min_move = jj

                        # set min_move to the new min
                        self.board.undo()
                # Set the best_move to max of
                # min_move and best_move
                if(best_score < min_score):
                    best_score = min_score
                    best_move = ii

                self.board.undo()
        move = best_move
        try:
            self.board.make_move(move, self.color)
        except InvalidMoveError:
            pass
        return move

    def board_score(self):
        w_points = 0
        b_points = 0
        for c in range(self.col):
            for r in range(self.row):
                if self.board.board[c][r].get_color() == self.color:
                    if self.board.board[c][r].is_king == True:
                        w_points += 1.2
                    else:
                        w_points += 1
                elif self.board.board[c][r].get_color() == self.opponent[self.color]:
                    if self.board.board[c][r].is_king == True:
                        b_points += 1.2
                    else:
                        b_points += 1
                else:
                    pass
        return w_points - b_points
