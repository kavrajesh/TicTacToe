## Tic Tac Toe v1.1 by Kavya Rajesh and Mounica Akula

## Current Version Rules/Capabilities:
# 1. Only two-player option available
# 2. Currently does not account for ties
# 3. Data validation and Error handling in place where necessary
# 4. Illegal moves are not allowed (i.e. cannot play a position that is already filled)

## Board Representation
board = []
for i in range(10):
  board.append(" ")

def print_board():
    print (board[0] + " | "+board[1] + " | "+board[2] )
    print ("--+--" + "-+---" )
    print (board[3] + " | "+board[4] + " | "+board[5] )
    print ("--+--" + "-+---" )
    print (board[6] + " | "+board[7] + " | "+board[8] )

## Win Logic Component
wins = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

## Player Moves
# Player 1
def player1_move():
  p1_move = input("Player 1, Choose position on board (between 1 - 9): ")
  #Integer data validation
  try:
    p1_move = int(p1_move)
  except ValueError:
    print("\nPlease make sure you have entered an integer between 1 - 9\n")
    player1_move()
  # Index Range data validation
  if p1_move > 9 or p1_move < 1:
    print("\nPlease make sure to enter an integer values that fall between 1 - 9\n")
    player1_move()
  # Handling Illegal Moves 
  elif board[int(p1_move) - 1] != " ":
    print("\nThis position is already filled. Please pick another spot!\n")
    player1_move()
  else:
    board[int(p1_move) - 1] = player1_character
    print("\n")
    print_board()
    print("\n")
    # Win Logic
    isWin = False
  for list in wins:
    if board[list[0]-1] != " " and board[list[0]-1] == board[list[1]-1] and board[list[1]-1] == board[list[2]-1]:
      isWin = True 
      break 
    else:
      continue        
  if isWin:
    print("Game over, Player 1 has Won!") 
  else:  
    player2_move()

# Player 2  
def player2_move():
  p2_move = input("Player 2, Choose position on board (between 1 - 9): ")
  #Integer data validation
  try:
    p2_move = int(p2_move)
  except ValueError:
    print("\nPlease make sure you have entered an integer between 1 - 9\n")
    player2_move()
  # Index Range data validation
  if p2_move > 9 or p2_move < 1:
    print("\nPlease make sure to enter an integer values that fall between 1 - 9\n")
    player2_move()
  # Handling Illegal Moves  
  elif board[int(p2_move) - 1] != " ":
    print("\nThis position is already filled. Please pick another spot!\n")
    player2_move()
  else:
    board[int(p2_move) - 1] = player2_character
    print("\n")
    print_board()
    print("\n")
    # Win Logic
    isWin = False
  for list in wins:
    if board[list[0]-1] != " " and board[list[0]-1] == board[list[1]-1] and board[list[1]-1] == board[list[2]-1]:
      isWin = True 
      break  
    else:
      continue
  if isWin:
    print("Game over, Player 2 has Won!") 
  else:
    player1_move()
  
## Instruction Board  
print ("1" + " | "+"2" + " | "+"3" )
print ("--+--" + "-+---" )
print ("4" + " | "+"5" + " | "+"6" )
print ("--+--" + "-+---" )
print ("7" + " | "+"8" + " | "+"9\n")

print("Lets Play TicTacToe!\n")
player1_character = input("Player 1, Pick your character (X or O): ").upper()

## Character Validation
if player1_character.upper() != "X" and player1_character.upper() != "O":
  print("\nPlease either select 'X' or 'O' as your character\n")
  player1_character = input("Player 1, Pick your character (X or O): ").upper()
if player1_character == "0":
  print("\nPlease either select 'X' or 'O' as your character\n")
  player1_character = input("Player 1, Pick your character (X or O): ").upper()

## Character Assignment
if player1_character == "X" :
  player2_character = "O"
else:
  player2_character = "X" 

print("\nPlayer 1 is "+ player1_character)
print("\nPlayer 2 is "+ player2_character +"\n")

player1_move()
