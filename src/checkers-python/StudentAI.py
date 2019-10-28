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
        moves = self.board.get_all_possible_moves(self.color) # list of moves

        #best_move = moves[0][0]
        # for i in moves:
        #   min_move = moves[0][1]
        #   self.make_move(i)
        #   for j in self.board.get_all_possible_moves(opponent_color)
        #         self.make_move(j)
        #         min(min_move, j.score)
        #         self.undo() # Undo the last move
        #   max(best_move, moves)
        #   self.undo()
        # move= bestmove

        best_move = moves[0][0]
        for i in moves:
            self.board.make_move(i)
            opponents_moves = self.board.get_all_possible_moves(self.opponent[self.color])
            min_move = opponents_moves[0][0];
            for j in opponents_moves:
                self.board.make_move(j)
                # Find the min between min_move and j
                # set min_move to the new min
                self.board.undo()
            # Set the best_move to max of 
            # i and best_move
            self.board.undo()
        #move = best_move
        self.board.make_move(move,self.color)
        return move

    def checkscore(self):
        return 0
    