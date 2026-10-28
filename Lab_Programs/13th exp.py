# Minimax Algorithm for Tic-Tac-Toe

def minimax(board, is_max):
    if check_win(board, 'X'):
        return 1
    if check_win(board, 'O'):
        return -1
    if ' ' not in board:
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, minimax(board, False))
                board[i] = ' '
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, minimax(board, True))
                board[i] = ' '
        return best


def check_win(board, p):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(board[a] == board[b] == board[c] == p
               for a,b,c in wins)


board = [' '] * 9

while True:
    print("\n", board[0:3], "\n", board[3:6], "\n", board[6:9])

    # Human player
    pos = int(input("Enter position (1-9): ")) - 1

    if pos not in range(9) or board[pos] != ' ':
        print("Invalid move!")
        continue

    board[pos] = 'O'

    if check_win(board, 'O'):
        print("You win!")
        break
    if ' ' not in board:
        print("Draw!")
        break

    # Computer uses Minimax
    best_score = -100
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 'X'
    print("Computer chooses position:", best_move + 1)

    if check_win(board, 'X'):
        print("Computer wins!")
        break
    if ' ' not in board:
        print("Draw!")
        break

print("\nFinal Board:")
print(board[0:3])
print(board[3:6])
print(board[6:9])
