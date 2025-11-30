class TicTacToe:
    def __init__(self):
        self.board = """
 {s1:^3} | {s2:^3} | {s3:^3}
-----+-----+-----
 {s4:^3} | {s5:^3} | {s6:^3}
-----+-----+-----      123
 {s7:^3} | {s8:^3} | {s9:^3}       456
                       789  
"""
        self.play = self.initialize_board()
        self.players = {1:"x", 2:"o"}
        winner = self.play_game()
        if winner == None:
            print("Draw")
        else:
            print(f"The winner is player {winner}")

    def initialize_board(self):
        play = {}
        for n in range(9):
            play["s{}".format(n+1)] = ""
        return play
    
    def show_board(self):
        """ display the playing board.  We take a dictionary with the current state of the board
        We rely on the board string to be a global variable"""
        print(self.board.format(**self.play))

    def get_move(self, n, xo):
        """ ask the current player, n, to make a move -- make sure the square was not 
        already played.  xo is a string of the character (x or o) we will place in
        the desired square """
        valid_move = False
        valid_squares = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while not valid_move:
            idx = input("player {}, enter your move (1-9)".format(n))
            if idx not in valid_squares:
                print(f"{idx} is an invalid spot")
                continue
            if self.play["s{}".format(idx)] == "":
                valid_move = True
            else:
                print("invalid: {}".format(self.play["s{}".format(idx)]))            
            
        self.play["s{}".format(idx)] = xo
    
    def play_game(self):
        self.show_board()
        winner = None
        for move in range(9):
            self.get_move(move%2+1, self.players[move%2+1])
            self.show_board()
            if move < 4:
                continue
            else:
                for i in range(3):
                    #print(self.play[f"s{i+1}"]== self.play[f"s{i+2}"]== self.play[f"s{i+3}"])
                    #print(self.play[f"s{i+1}"]== self.play[f"s{i+4}"]== self.play[f"s{i+7}"])
                    if self.play[f"s{3*i+1}"] == self.play[f"s{3*i+2}"] == self.play[f"s{3*i+3}"] != "":
                        winner = self.play[f"s{3*i+1}"]
                        break
                    if self.play[f"s{i+1}"] == self.play[f"s{i+4}"] == self.play[f"s{i+7}"] != "":
                        winner = self.play[f"s{i+1}"]
                        break
                if (self.play[f"s{1}"] == self.play[f"s{5}"] == self.play[f"s{9}"]) or \
                   (self.play[f"s{3}"] == self.play[f"s{5}"] == self.play[f"s{7}"]):
                    winner = self.play[f"s{5}"]
            if winner != None:
                break
            
        else:
            return None
        
        if self.players[1] == winner:
            return 1
        else:
            return 2

if __name__ == "__main__":
    TicTacToe()