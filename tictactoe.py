from enum import IntEnum


class TicTacToe:
    def __init__(self):
        self.board = []

    class STATES(IntEnum):
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4

    def create_board(self):  # initial creation of the board
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)
        if self.board:
            return True

    def place_marker(self, symbol, row, column):  # places users symbol on board
        if symbol == "x":
            if (row > 2 or row < 0) or (column > 2 or column < 0):  # checks if input is in range
                players_turn = self.STATES(0)
                print("Column/row input is out of range, values must range from 0-2")
                return players_turn.name
            if self.board[row][column] != "-":  # check for duplicate space
                players_turn = self.STATES(0)
                print("Space is already taken, please choose another")
                return players_turn.name
            else:
                self.board[row][column] = symbol
                players_turn = self.STATES(1)
                return players_turn.name

        if symbol == "o":
            if (row > 2 or row < 0) or (column > 2 or column < 0): # checks if input is in range
                players_turn = self.STATES(1)
                print("Column/row input is out of range, values must range from 0-2")
                return players_turn.name
            if self.board[row][column] != "-":  # check for duplicate space
                players_turn = self.STATES(1)
                print("Space is already taken, please choose another")
                return players_turn.name
            else:
                self.board[row][column] = symbol
                players_turn = self.STATES(0)
                return players_turn.name

    def output_board(self):  # displays board
        for row in self.board:
            for value in row:
                print(value, end=" ")
            print()

    def check_winner(self):  # checks winning combinations of 3x3 board
        if self.board[0][0] == "x" and self.board[1][0] == "x" and self.board[2][0] == "x":  # left column win for x
            winner = self.STATES(3)
            return winner.name
        elif self.board[0][0] == "o" and self.board[1][0] == "o" and self.board[2][0] == "o":  # left column win for o
            winner = self.STATES(4)
            return winner.name
        elif self.board[0][1] == "x" and self.board[1][1] == "x" and self.board[2][1] == "x":  # middle column win for x
            winner = self.STATES(3)
            return winner.name
        elif self.board[0][1] == "o" and self.board[1][1] == "o" and self.board[2][1] == "o":  # middle column win for o
            winner = self.STATES(4)
            return winner.name
        elif self.board[0][2] == "x" and self.board[1][2] == "x" and self.board[2][2] == "x":  # right column win for x
            winner = self.STATES(3)
            return winner.name
        elif self.board[0][2] == "o" and self.board[1][2] == "o" and self.board[2][2] == "o":  # right column win for o
            winner = self.STATES(4)
            return winner.name
        elif self.board[0][0] == "x" and self.board[0][1] == "x" and self.board[0][2] == "x":  # first row win for x
            winner = self.STATES(3)
            return winner.name
        elif self.board[0][0] == "o" and self.board[0][1] == "o" and self.board[0][2] == "o":  # first row win for o
            winner = self.STATES(4)
            return winner.name
        elif self.board[1][0] == "x" and self.board[1][1] == "x" and self.board[1][2] == "x":  # second row win for x
            winner = self.STATES(3)
            return winner.name
        elif self.board[1][0] == "o" and self.board[1][1] == "o" and self.board[1][2] == "o":  # second row win for o
            winner = self.STATES(4)
            return winner.name
        elif self.board[2][0] == "x" and self.board[2][1] == "x" and self.board[2][2] == "x":  # third row win for x
            winner = self.STATES(3)
            return winner.name
        elif self.board[2][0] == "o" and self.board[2][1] == "o" and self.board[2][2] == "o":  # third row win for o
            winner = self.STATES(4)
            return winner.name
        elif self.board[0][0] == "x" and self.board[1][1] == "x" and self.board[2][2] == "x":  # left diagonal win for x
            winner = self.STATES(3)
            return winner.name
        elif self.board[0][0] == "o" and self.board[1][1] == "o" and self.board[2][2] == "o":  # left diagonal win for o
            winner = self.STATES(4)
            return winner.name
        elif self.board[0][2] == "x" and self.board[1][1] == "x" and self.board[2][0] == "x":  # right diagonal win for x
            winner = self.STATES(3)
            return winner.name
        elif self.board[0][2] == "o" and self.board[1][1] == "o" and self.board[2][0] == "o":  # right diagonal win for o
            winner = self.STATES(4)
            return winner.name
        else:
            return False

    def check_draw(self):  # checks if there is a tie
        count = 0
        for row in self.board:
            for value in row:
                if value == "-":
                    count += 1
        if count == 0:
            is_draw = self.STATES(2)
            return is_draw.name
        else:
            return False

    def run_game(self):  # main function that runs the game
        players_turn = ""
        game_won = False
        x_variable = "x"
        o_variable = "o"
        print("Player 1 please enter your symbol of choice(x or o)")
        player_symbol = input("Choice: ")
        if player_symbol == "x" or player_symbol == "o":
            self.create_board()
            self.output_board()
            print("Now, enter the Row you would like to place your symbol(0-2)")
            input_row = int(input())
            print("Now, enter the Column you would like to place your symbol(0-2)")
            input_column = int(input())
        else:
            print("Invalid input, input value must be 'x' or 'o'")
            self.run_game()

        while game_won == False:  # function stays in loop till a winner/draw is declared

            if players_turn == "CROSS_TURN":
                player_symbol = x_variable
                print("x's turn")
                print("Now, enter the Row you would like to place your symbol(0-2)")
                input_row = int(input())
                print("Now, enter the Column you would like to place your symbol(0-2)")
                input_column = int(input())

            elif players_turn == "NAUGHT_TURN":
                player_symbol = o_variable
                print("o's turn")
                print("Now, enter the Row you would like to place your symbol(0-2)")
                input_row = int(input())
                print("Now, enter the Column you would like to place your symbol(0-2)")
                input_column = int(input())
            players_turn = self.place_marker(player_symbol, input_row, input_column)
            self.output_board()
            champion = self.check_winner()  # check for winner after every move
            if champion == "CROSS_WON":
                print("X is the winner!!!")
                game_won = True
            elif champion == "NAUGHT_WON":
                print("O is the winner!!!")
                game_won = True
            elif champion == False:
                draw = self.check_draw()
                if draw == "DRAW":
                    print("Draw, no one is the winner")
                    game_won = True


if __name__ == '__main__':  # begins game
    user_input = TicTacToe()
    user_input.run_game()