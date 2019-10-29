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
            			self.board.make_move(jj, self.opponent[self.color])
						# Find the min between min_move and j
                        if( min_score > self.board_score() ):
                            min_score = self.board_score
                            min_move = jj

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
	
	def board_score(self, color):
        ## @param color: color of player making the move
        ## Heuristics to Evaluate with
        ## Normal Piece : 1000 pts
        ## King Piece : 2000 pts
        ## Rows away from enemy end if Normal : (rows - curr_row / rows) * 1000
        ## Amount of Pieces : (Amount of pieces left) / (self.col * self.p / 2) * 100
        ## Randomization : randomInt (0-10)
        
		player_points = 0
		opponent_points = 0
		for c in range(self.col):
			for r in range(self.row):
				current_piece = self.board.board[c][r]

                if current_piece.get_color() == color:
					if current_piece.is_king == True:
						player_points += 2000
					else:
						player_points += 1000
                        if color == 1:
                            player_points += ((self.row - r) / self.row) * 1000
                        else:
                            player_points += (r / self.row) * 1000
                elif current_piece.get_color() == self.opponent[color]:
					if current_piece.is_king == True:
						opponent_points += 2000
					else:
						opponent_points += 1000
                        if self.opponent[color] == 1:
                            opponent_points += ((self.row - r) / self.row) * 1000
                        else:
                            opponent_points += (r / self.row) * 1000
                else:
					pass
        
        if color == 1:
            player_points += ((self.board.white_count / (self.col * self.p / 2)) * 100)
            opponent_points += ((self.board.black_count / (self.col * self.p / 2)) * 100)
        else:
            player_points += ((self.board.black_count / (self.col * self.p / 2)) * 100)
            opponent_points += ((self.board.white_count / (self.col * self.p / 2)) * 100)
        
        randomization = randint(0, 50)
            
		return player_points - opponent_points + randomization
