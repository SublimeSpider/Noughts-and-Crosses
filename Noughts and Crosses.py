import os
from time import sleep
import csv

def displayboard(board):
    print(" ", board[0][0], "│", board[0][1], "│", board[0][2])
    print("──┼──┼──")
    print(" ", board[1][0], "│", board[1][1], "│", board[1][2])
    print("──┼──┼──")
    print(" ", board[2][0], "│", board[2][1], "│", board[2][2])

def check_win(board, player):
    won = False
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        won = True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        won = True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        won = True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        won = True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        won = True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        won = True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        won = True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        won = True
    return(won)

def take_turn(board, player, GameName):
    print(player,"it is your turn")
    displayboard(board)
    try:
        Ycoordinate = int(input("Please enter the row you would like to play on : "))
    except TypeError:
        print("Please enter an integer value of 1,2, or 3\n")
        take_turn(board, player)
    if (Ycoordinate != 1) and (Ycoordinate != 2) and (Ycoordinate != 3):
        print("Please enter an integer value of 1,2, or 3\n")
        take_turn(board, player)
    Ycoordinate = Ycoordinate - 1
    try:
        Xcoordinate = int(input("Please enter the column you would like to play on : "))
    except TypeError:
        print("Please enter an integer value of 1,2, or 3\n")
        take_turn(board, player)
    if (Xcoordinate != 1) and (Xcoordinate != 2) and (Xcoordinate != 3):
        print("Please enter an integer value of 1,2, or 3\n")
        take_turn(board, player)
    Xcoordinate = Xcoordinate - 1
    if (board[Ycoordinate][Xcoordinate] != "X") and (board[Ycoordinate][Xcoordinate] != "O"):
        board[Ycoordinate][Xcoordinate] = player
    else:
        try_player = player
        print("This space is taken please try again")
        take_turn(board, try_player)
    won = check_win(board, player)
    quiting = input("Would you like to quit this game? (Y/N) : ")
    if (quiting == "Y") and (won == False):
        won = str("Y")
    with open(GameName, 'w') as f: 
        write = csv.writer(f) 
        write.writerows(board)
    return won

def game(board, GameName):
    player = "X"
    for attempts in range(0,9):
        won = take_turn(board, player, GameName)
        if won == True:
            print("Well done,",player,"you win")
            break
        elif won == "Y":
            print("Exiting game")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"
    if won == False:
        print("Draw")
        
def Quit():
    print("Quit")
    exit()

def ResumeGame():
    print("Resume game")
    path = ("C:\\Users\\Alan\\Documents\\Seth_Documents\\School\\Computer_Science\\Noughts and Crosses")
    files = os.listdir(path)
    print("The following saved games are available:")
    for file in files:
        if file[-3:] == "csv":
            print("             "+file[:-4])
    GameName = input("Please enter the games name : ")
    GameName = GameName+".csv"
    with open(GameName, 'r') as read_obj:
        csv_reader = csv.reader(read_obj) 
        board = list(csv_reader)
        board = [x for x in board if x != []]
    wonX = check_win(board, "X")
    wonO = check_win(board, "O")
    PossibleAttempts = 0
    for number in range(0,3):
        if (board[number][0] != "X") and (board[number][0] != "O"):
            PossibleAttempts = PossibleAttempts + 1
        elif (board[number][1] != "X") and (board[number][1]) != "O":
            PossibleAttempts = PossibleAttempts + 1
        elif (board[number][2] != "X") and (board[number][2] != "O"):
            PossibleAttempts = PossibleAttempts + 1
        player = "X"
    for attempts in range(0, PossibleAttempts):
        won = take_turn(board, player, GameName)
        if won == True:
            print("Well done,",player,"you win")
            break
        elif won == "Y":
            print("Exiting game")
            break
            if player == "X":
                player = "O"
            else:
                player = "X"
        if won == False:
            print("Draw")
    menu()

def NewGame():
    board = [["   ", "    ", "   "],["   ","    ", "   "],["   ", "    ", "   "]]
    print("New game")
    GameName = input("Please enter the games name : ")
    GameName = GameName+".csv"
    file = open(GameName, "w")
    game(board, GameName)
    with open(GameName, 'w') as f: 
        write = csv.writer(f) 
        write.writerows(board)
    menu()

def Instructions():
    print("Instructions")
    print("\nThe first player will draw a nought or a cross in one block.")
    print("\nEach person takes a turn trying to make a row of three either across, down, or diagonally, and at the same time tries to prevent their opponent from doing the same.")
    print("\nThe first person to make three noughts or three crosses in a row is the winner.\n")
    menu()

def menu():
    try:
        print("\n************************************************************************************************************************\n")
        MenuOption = int(input("Would you like to 1. Read the instructions, 2. Start a new game, 3. Resume an existing game or, 4. Quit : "))
        print("\n************************************************************************************************************************\n")
    except TypeError:
        print("Please enter a 1, 2, 3, or a 4\n")
        menu()
    if (MenuOption != 1) and (MenuOption != 2) and (MenuOption != 3) and (MenuOption != 4):
        print("Please enter a 1, 2, 3, or a 4\n")
        menu()
    if MenuOption == 1:
        Instructions()
    elif MenuOption == 2:
        NewGame()
    elif MenuOption == 3:
        ResumeGame()

menu()
