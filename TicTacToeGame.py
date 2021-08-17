'''
Tic Tac Toe Program using classes
'''

import os
os.system('clear')

class Board:

    def __init__(self):
        self.cells = [" ", " "," ", " "," ", " "," ", " "," ", " "]

    def display(self):
        print(" %s | %s | %s "%(self.cells[1],self.cells[2],self.cells[3]))
        print("-----------")
        print(" %s | %s | %s "%(self.cells[4],self.cells[5],self.cells[6]))
        print("-----------")
        print(" %s | %s | %s "%(self.cells[7],self.cells[8],self.cells[9]))

    def print_header(self):
        print("Welcome to Tic Tac Toe Game")

    def refresh_screen(self):
        os.system('cls')
        self.print_header()
        self.display()
    
    def update_cell(self,pos,player):
        if self.cells[pos] == ' ':
            self.cells[pos] = player

    def validate_pos(self,pos):
        if pos < 1 or pos > 9:
            print("Invalid Cell Position. Please enter board position from 1 to 9.")
            return False
        else: 
            return True
            
    def is_winner(self,player):
        if (self.cells[1] == player and self.cells[2] == player and self.cells[3] == player):
            return True
        elif (self.cells[4] == player and self.cells[5] == player and self.cells[6] == player):
            return True
        elif (self.cells[7] == player and self.cells[8] == player and self.cells[9] == player):
            return True
        elif (self.cells[7] == player and self.cells[8] == player and self.cells[9] == player):
            return True
        elif (self.cells[1] == player and self.cells[4] == player and self.cells[7] == player):
            return True
        elif (self.cells[2] == player and self.cells[5] == player and self.cells == player):
            return True
        elif (self.cells[3] == player and self.cells[6] == player and self.cells[9] == player):
            return True
        elif (self.cells[1] == player and self.cells[5] == player and self.cells[9] == player):
            return True
        elif (self.cells[3] == player and self.cells[5] == player and self.cells[7] == player):
            return True
        else:
            return False

    def is_tie(self):
        count = 0
        for c in self.cells:
            if c != ' ':
                count += 1
        if (count == 9):
            return True
        else:
            return False


    def reset(self):
        self.cells = [" ", " "," ", " "," ", " "," ", " "," ", " "]


b = Board()

while True:
    b.refresh_screen()

    # Get X Input
    x_choice = int(input("(\nX)  Please choose 1 - 9 -> "))

    b.update_cell(x_choice, 'X')

    b.refresh_screen()
    
    if (b.is_winner('X')):
        print('X Wins!')
        start_game = input(' Do you want to start a new game (Y/N) -> ').lower()
        if (start_game == 'y'):
            b.reset()
            continue
        else:
            break

    #Game tie
    if (b.is_tie()):
        print('It is a tie!')
        start_game = input(' Do you want to start a new game (Y/N) -> ').lower()
        if (start_game == 'y'):
            b.reset()
            continue
        else:
            break


    #o_choice = b.validate_pos(o_choice)

    o_choice = int(input("(\nO)  Please choose 1 - 9 -> "))

    b.update_cell(o_choice, 'O')

    b.refresh_screen()


    if (b.is_winner('O')):
        print('O Wins!')
        start_game = input(' Do you want to start a new game (Y/N) -> ').lower()
        if (start_game == 'y'):
            b.reset()
            continue 
        else:
            break 

    if (b.is_tie()):
        print('It is a tie!')
        start_game = input(' Do you want to start a new game (Y/N) -> ').lower()
        if (start_game == 'Y'):
            b.reset()
            continue
        else:
            break 






    
    
    
