import os

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

player_x_moves = []
player_o_moves = []
occupied_position = []

final_result = ...

win_conditions = [
                [0,1,2], [3,4,5], [6,7,8], 
                [0,3,6], [1,4,7], [2,5,8], 
                [0,4,8], [2,4,6]
                ]

def board_display():
    # Function to display the current state of the board
    print(row1)
    print(row2)
    print(row3)

def position_choice():
    # Function to get the player's choice of position
    choice = ''
    while not choice.isdigit():
        board_display()
        print("type one number between 1 and 9:")
        choice = input("-> ")
        if not choice.isdigit() or  0 <= int(choice) > 9:
            os.system("cls")
            print("you have to type a valid number...")
            choice = ''
    return int(choice)

def check_position(position):
    # Function to check if the chosen position is already occupied
    if position in occupied_position:
        os.system("cls")
        print("this play already has been chosen ...")
        print("make your choice again:")
        return False
    return True

def check_winner(win_combos, x_moves, o_moves): # function who decide who wins
    for item in win_combos:
        # Check if all positions in the winning combination are occupied by player O
        if all(pos in x_moves for pos in item):
            return 'X Victory'
        # Check if all positions in the winning combination are occupied by player O
        if all(pos in o_moves for pos in item): 
            return 'O Victory'
        
def tictac_toe():
    turn = 1
    player = ''
    while turn != 10:
        # the turn decision
        if turn % 2 != 0:
            player = 'X'
            print("it's player X time")
        else:
            player = 'O'
            print("it's player O time")
        # the choice for the positoin happens here
        position = position_choice()
        # here the append happen to store the positions, for in the final decide who won the game
        if player == 'X':
            player_x_moves.append(position-1)
        else:
            player_o_moves.append(position-1)
        # checks if the play is already chosen
        if check_position(position):
            occupied_position.append(position)
        else:
            continue
        # here is where de play is made
        if 1 <= position <= 3:
            row1[position - 1] = player
        elif 3 <= position <= 6:
            row2[position - 4] = player
        elif 7 <=position <= 9:
            row3[position - 7] = player
        # check if anyone won
        final_result = check_winner(win_conditions, player_x_moves, player_o_moves)
        if final_result:
            print(f"The final result is {final_result}!!")
            break
        # clean the display
        os.system("cls")
        # change the turn
        turn += 1
tictac_toe()

board_display()