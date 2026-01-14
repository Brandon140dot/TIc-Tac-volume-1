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



def check_winner(board, player_symbol):
  
  for row in board:
    if row[0] == player_symbol and row[1] == player_symbol and row[2] == player_symbol:
      return True

 
  for col in range(3):
    if board[0][col] == player_symbol and board[1][col] == player_symbol and board[2][col] == player_symbol:
      return True


  if board[0][0] == player_symbol and board[1][1] == player_symbol and board[2][2] == player_symbol:
    return True

  if board[0][2] == player_symbol and board[1][1] == player_symbol and board[2][0] == player_symbol:
    return True

  return False



def check_tie(board):
  for row in board:
    for spot in row:
      if isinstance(spot, int):
        return False
  return True



def play_game():
  board = create_board()
  current_player = "X"

  while True:
    display_board(board)

    choice = get_player_choice(current_player)
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

