import random


def create_board():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def display_board(board):
    for row in board:
        print(row)


def get_player_choice():
    choice = int(input("Choose a number (1-9): "))
    return choice


def get_robot_choice(board):
    numbers = []

    for row in board:
        for spot in row:
            if type(spot) == int:
                numbers.append(spot)

    return random.choice(numbers)


def place_move(board, choice, symbol):
    for row in board:
        for i in range(3):
            if row[i] == choice:
                row[i] = symbol


def check_winner(board, symbol):
    for row in board:
        if row[0] == symbol and row[1] == symbol and row[2] == symbol:
            return True

    for col in range(3):
        if board[0][col] == symbol and board[1][col] == symbol and board[2][col] == symbol:
            return True

    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True

    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True

    return False


def check_tie(board):
    for row in board:
        for spot in row:
            if type(spot) == int:
                return False
    return True


def play_game():
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)

        if current_player == "X":
            choice = get_player_choice()
        else:
            choice = get_robot_choice(board)
            print("Robot chose:", choice)

        place_move(board, choice, current_player)

        if check_winner(board, current_player):
            display_board(board)
            print(current_player, "wins!")
            break

        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


play_game()
