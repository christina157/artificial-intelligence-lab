import random

stones = 10

while stones > 0:
    print("\nStones remaining:", stones)

    # Player's turn
    move = int(input("Take 1, 2, or 3 stones: "))

    if move not in [1, 2, 3] or move > stones:
        print("Invalid move! Try again.")
        continue

    stones -= move

    if stones == 0:
        print("You win!")
        break

   # Computer's turn
    computer_move = (stones - 1) % 4

    if computer_move == 0 or computer_move > 3:
        computer_move = random.randint(1, min(3, stones))

    print("Computer takes", computer_move, "stones.")
    stones -= computer_move

    if stones == 0:
        print("Computer wins!")
