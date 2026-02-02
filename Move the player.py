import random
# making the matrix
matrix = [['*' for x in range(5)] for b in range(5)]

def coordinate_checker(row: int, col: int):
    return 0 <= row <= 4 and 0 <= col <= 4

# Welcome message and rules of the game
print("*" * 10, "Welcome to the simple player game!", "*" * 10)
print()
print("To play,you must choose one of the following commands: 'down, up, left, right!'")
print(f"Make sure you guide the player 'P' to the final destination, marked with 'X'")
print("or, to stop the game, please enter: 'end'. ")
print("Be careful though! There are bombs, marked with the symbol 'B', which will kill you if you step on them!")
print()

# making sure bombs and player exit are not in the same position
while True:
    first_bomb = [random.randint(1, 4) for _ in range(2)]
    second_bomb = [random.randint(1, 4) for _ in range(2)]
    player_exit = [random.randint(1, 4) for _ in range(2)]

    if first_bomb == second_bomb:
        continue
    if player_exit == first_bomb or player_exit == second_bomb:
        continue
    else:
        break

# player position
# player's position always starts at the first row, so it doesn't conflict with the exit or the bombs
player_col_y1 = random.randint(1, 4)
starting_player_position = [0, player_col_y1]

# directions, which player can move
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}
#updating coordinates for player and bombs
matrix[starting_player_position[0]][starting_player_position[1]] = "P"
matrix[first_bomb[0]][first_bomb[1]] = "B"
matrix[second_bomb[0]][second_bomb[1]] = "B"
matrix[player_exit[0]][player_exit[1]] = "X"
# finding player position
player_location = tuple()
for r in range(5):
    for c in range(5):
        if matrix[r][c] == "P":
            player_location = (r, c)

# starting the game
while True:

    for row in range(5):
        print(matrix[row])

    command = input("Choose an action to perform: ") # player will enter four directions: down,up,left,right

    if command == "end":
        print("Thank you for playing!")
        break

    if command not in ["down", "up", "left", "right"]:
        print("Please try another command!")
        continue

    else:
         move = directions[command]
         next_row =  player_location[0] + move[0]
         next_col = player_location[1] + move[1]

         if coordinate_checker(next_row, next_col):
             if matrix[next_row][next_col] == "*":
                 matrix[next_row][next_col] = "P"
                 matrix[player_location[0]][player_location[1]] = "*"
                 player_location = (next_row, next_col)
             elif matrix[next_row][next_col] == "B":
                 print("Game over!")
                 print("Player stepped on a bomb and died :(")
                 break
             elif matrix[next_row][next_col] == "X":
                 print("You win!")
                 print("Player successfully escaped")
                 break
         else:
             print("You can't go there!")
             continue