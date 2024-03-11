"""
Program: game tic-tac-toe with numbers, Two players take turns entering a number and
         entering the position they want to put the number in and the first player
         that gets the sum of any horizontal or vertical or diagonal line to 15 wins
         player 1's list is [1,3,5,7,9]
         player 2's list is [0,2,4,6,8]
Author: Abdelrahman Akram Kamal al din
date created: 1st of March 2024
"""

while True:
    # while loop to keep the game running as desired
    print("Welcome to tic-tac-toe with numbers game.")
    states = ['A', 'B']
    state = input("A) Play game\nB) Quit game\n").upper()
    # check input validation
    while state not in states:
        state = input("Invalid input please enter one of the two letters. \nA) Play game\nB) Quit game").upper()
    if state == 'A':
        board = ['-', '-', '-',
                 '-', '-', '-',
                 '-', '-', '-']
        # declare variables
        current_player = 1
        winner = None
        list1 = [1, 3, 5, 7, 9]
        str_list1 = ['1', '3', '5', '7', '9']
        list2 = [0, 2, 4, 6, 8]
        str_list2 = ['0', '2', '4', '6', '8']
        game_running = True

        # function to print the board
        def print_board(board):
            for i in range(9):
                board[i] = str(board[i])
            print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
            print(" -------------")
            print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
            print(" -------------")
            print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " |  ")
            print("              \n")
            for i in range(9):
                if board[i] != '-':
                    board[i] = int(board[i])

        # function to get inputs
        def get_input(board):
            cell_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            global list1
            global current_player
            global str_list1
            global list2
            global str_list2
            print(f"It's player {current_player}' turn")
            cell = input(
                # the location of the number
                "Enter the number of the cell you want to put your number in (starting from 1 to 9 from the top left)")
            # check if cell is a positive integer or not
            while not cell.isnumeric() or cell not in cell_list:
                cell = input("Invalid input please enter a valid input : ")
            cell = int(cell)
            # get input for player 1
            if current_player == 1:
                print("Your available numbers are : ", list1)
                num1 = input("Please enter a number from your list : ")
                num1 = str(num1)
                while num1 not in str_list1:
                    num1 = input("Invalid input please enter a number from your list : ")
                str_list1.remove(num1)
                num1 = int(num1)
                list1.remove(num1)
                r_cell = cell - 1
                board[r_cell] = num1
                # get input for player 2
            elif current_player == 2:
                print("Your available numbers are : ", list2)
                num2 = input("Please enter a number from your list : ")
                num2 = str(num2)
                while num2 not in str_list2:
                    num2 = input("Invalid input please enter a number from your list : ")
                str_list2.remove(num2)
                num2 = int(num2)
                list2.remove(num2)
                r_cell = cell - 1
                board[r_cell] = num2
            return board

        # check horizontal lines to see if someone won
        def check_horizontal(board):
            global winner
            if board[1] != '-' and board[2] != '-' and board[0] != '-' and board[0] + board[1] + board[2] == 15:
                winner = current_player
                return True
            elif board[3] != '-' and board[4] != '-' and board[5] != '-' and board[3] + board[4] + board[5] == 15 and \
                    board[
                        3] != '-':
                winner = current_player
                return True
            elif board[6] != '-' and board[7] != '-' and board[8] != '-' and board[6] + board[7] + board[8] == 15 and \
                    board[
                        6] != '-':
                winner = current_player
                return True

        # check vertical lines to see if someone won
        def check_vertical(board):
            global winner
            if board[0] != '-' and board[3] != '-' and board[6] != '-' and board[0] + board[3] + board[6] == 15 and \
                    board[
                        3] != '-':
                winner = current_player
                return True
            elif board[1] != '-' and board[4] != '-' and board[7] != '-' and board[1] + board[4] + board[7] == 15 and \
                    board[
                        1] != '-':
                winner = current_player
                return True
            elif board[2] != '-' and board[5] != '-' and board[8] != '-' and board[2] + board[5] + board[8] == 15 and \
                    board[
                        2] != '-':
                winner = current_player
                return True

        # check diagonal lines to see if someone won
        def check_diagonal(board):
            global winner
            if board[0] != '-' and board[4] != '-' and board[8] != '-' and board[0] + board[4] + board[8] == 15 and \
                    board[
                        0] != '-':
                winner = current_player
                return True
            elif board[2] != '-' and board[4] != '-' and board[6] != '-' and board[2] + board[4] + board[6] == 15 and \
                    board[
                        2] != '-':
                winner = current_player
                return True

        # check if the game is a tie
        def check_tie(board):
            global game_running
            if '-' not in board:
                print_board(board)
                print("Its a tie! ")
                game_running = False

        # function to gather the previous functions that check wins in one function
        def check_win():
            global game_running
            if check_vertical(board) or check_diagonal(board) or check_horizontal(board):
                print_board(board)
                print(f"The winner is player {winner} ! ")
                game_running = False

        # function to switch players
        def switch_player():
            global current_player
            if current_player == 1:
                current_player = 2
            else:
                current_player = 1


        while game_running:
            print_board(board)
            get_input(board)
            check_win()
            check_tie(board)
            switch_player()
    elif state == 'B':
        break
