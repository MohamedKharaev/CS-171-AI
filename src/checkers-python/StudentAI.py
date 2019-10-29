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
        moves = self.board.get_all_possible_moves(self.color)
        best_move = moves[0][0]
        self.board.make_move(best_move, self.color)
        best_score = self.board_score()
        self.board.undo()

        for i in moves:
        	for ii in i:
				self.board.make_move(ii, self.color)
				opponents_moves = self.board.get_all_possible_moves(self.opponent[self.color])

				min_move = opponents_moves[0][0]
				self.board.make_move(min_move, self.opponent[self.color])
				min_score = self.board_score()
            	self.board.undo()

            	for j in opponents_moves:
            		for jj in j:
            			self.board.make_move(kk, self.opponent[self.color]__init__

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
		player_points = 0
		opponent_points = 0
		for c in range(self.col):
			for r in range(self.row):
				current_piece = self.board.board[c][r]
				if current_piece.get_color() == self.color:
					if current_piece.is_king == True:
						player_points += 1.2
					else:
						opponent_points += 1
				elif current_piece.get_color() == self.opponent[self.color]:
					if current_piece.is_king == True:
						opponent_points += 1.2
					else:
						opponent_points += 1
				else:
					pass
		return player_points - opponent_points
