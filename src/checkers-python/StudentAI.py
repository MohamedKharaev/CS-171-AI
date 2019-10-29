from random import randint
from BoardClasses import Move
from BoardClasses import Board
# The following part should be completed by students.
# Students can modify anything except the class name and exisiting functions and varibles.


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

        move = minMax(self.color, 2, best_score, best_move)
        self.board.make_move(move, self.color)
        return move

    def minMax(self, player, depth, best_score, best_move):
       	# base case depth = 0, return the score
    	if depth == 0:
            return self.board_score()
        # get all the moves of the current player
    	moves = self.board.get_all_possible_moves(player)
        # Itterate through each move
        for i in moves:
            for ii in i:
				# change to new game state
				self.board.make_move(ii, player)

				if (player == self.color):
					score2 = minMax(self, self.opponent[self.color], best_score, best_move)
					if (best_score < score2):
						best_score = score2
						best_move = ii
				elif(player == self.opponent[self.color]):
					score2 = minMax(self, self.color, best_score, best_move)
					if (best_score > score2):
						best_score = score2
						best_move = ii
				self.board.undo()
	return best_move

					


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
