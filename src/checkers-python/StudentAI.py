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
        #move = self.minMax(self.color, 4, -999999999, best_move, 999999999, best_move)[1]
        move = self.minMax2( self.color, 5, -999999999, 999999999, best_move )[1]
        self.board.make_move(move, self.color)

        return move
    
    def minMax(self, player, depth, best_score, best_move, opponent_score, opponent_move):
        if depth == 0:
            return self.board_score( ), best_move
        # get all the moves of the current player
        moves = self.board.get_all_possible_moves(player)
        # Itterate through each move
        for i in moves:
            for ii in i:
                # change to new game state
                self.board.make_move(ii, player)
                if (player == self.color):
                    opponent_score = self.minMax(self.opponent[self.color], depth-1, best_score, best_move,opponent_score, opponent_move)[0]
                    if (best_score <  opponent_score):
                        best_score = opponent_score
                        best_move = ii
                # opponent's turn: find the best score based on player's move
                elif (player == self.opponent[self.color]):
                    best_score = self.minMax(self.color, depth-1, best_score, best_move,opponent_score, opponent_move)[0]
                    if (opponent_score > best_score):
                        opponent_score = best_score
                        opponent_move = ii
                self.board.undo()
        return best_score, best_move, opponent_score, opponent_move

    def minMax2( self, player, depth, alpha, beta, best_move ):
        if depth == 0:
            return self.board_score(), best_move
            
        moves = self.board.get_all_possible_moves( player )
        if ( player == self.color ):
            player_score = -999999999 #MIN
            for i in moves: #Loop through possible moves
                for ii in i:
                    # switch to different game state
                    self.board.make_move( ii, player ) 
                    # Get opponents score in the game state
                    opponenet_score = self.minMax2( self.opponent[self.color], depth-1, alpha, beta, best_move )[0]
                    # max of best_score ( out of all moves ) and opponent score ( score for boardstate(ii) )
                    if( player_score <= opponenet_score ):
                        player_score = opponenet_score
                        best_move = ii
                    # pruning
                    alpha = max( alpha, player_score )
                    if( beta <= alpha ):
                        self.board.undo()
                        break
                    #undo board state
                    self.board.undo()
            return player_score, best_move
        else: # Poor-AI
            opponenet_score = 999999999 #MAX
            for i in moves:
                for ii in i:
                    # switch to different game state
                    self.board.make_move( ii, player )
                    # Get our AI score in the game state
                    player_score = self.minMax2( self.color, depth -1, alpha, beta, best_move )[0]
                    # min of best_score ( out of all moves ) and our AI's score ( score for boardstate(ii) )
                    opponenet_score = min( opponenet_score, player_score)
                    beta = min( beta, opponenet_score ) 
                    if( beta <= alpha ):
                        self.board.undo()
                        break
                     #undo board state

                    self.board.undo()
            return opponenet_score, best_move



    def board_score(self):
        ## @param color: color of player making the move
        ## Heuristics to Evaluate with
        ## Normal Piece : 1000 pts
        ## King Piece : 2000 pts
        ## Rows away from enemy end if Normal : (rows - curr_row / rows) * 1000
        ## Amount of Pieces : (Amount of pieces left) / (self.col * self.p / 2) * 100
        ## Randomization : randomInt (0-10)

        player_points = 0.0
        opponent_points = 0.0
        for c in range(self.col):
            for r in range(self.row):
                current_piece = self.board.board[c][r]

                if current_piece.get_color() == self.color:
                    if current_piece.is_king == True:
                        player_points += 2000
                    else:
                        player_points += 1000
                        if self.color == 2:
                            player_points += (self.row - r) * 200
                        else:
                            player_points += r  * 200
                else:
                    if current_piece.is_king == True:
                        opponent_points += 2000
                    else:
                        opponent_points += 1000
                        if self.opponent[self.color] == 2:
                            opponent_points += (self.row - r)* 200
                        else:
                            opponent_points += r * 200
        
        if self.color == 1:
            player_points += ((self.board.black_count / (self.col * self.p / 2)) * 100)
            opponent_points += ((self.board.white_count / (self.col * self.p / 2)) * 100)
        else:
            player_points += ((self.board.white_count / (self.col * self.p / 2)) * 100)
            opponent_points += ((self.board.black_count / (self.col * self.p / 2)) * 100)
        
        randomization = randint(0, 50)
        return player_points - opponent_points + randomization
