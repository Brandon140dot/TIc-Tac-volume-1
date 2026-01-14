def create_board():
  return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def display_board(board):
  for row in board:
    print(row)


board = create_board()
display_board(board)


def get_player_choice(player_symbol):
  choice = int(input("Player {player_symbol}, choose a number (1-9): "))
  return choice

def place_move(board, choice, player_symbol):
  for row in board:
    for i in range(3):
      if row[i] == choice:
        row[i] = player_symbol
