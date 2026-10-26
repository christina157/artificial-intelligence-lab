N = 8

board = [-1] * N

def is_safe(row, col):
    for prev_row in range(row):
        prev_col = board[prev_row]

        # Same column
        if prev_col == col:
            return False

        # Same diagonal
        if abs(prev_row - row) == abs(prev_col - col):
            return False

    return True


def solve(row):
    if row == N:
        print_board()
        return True

    for col in range(N):
        if is_safe(row, col):
            board[row] = col

            if solve(row + 1):
                return True

            # Backtrack
            board[row] = -1

    return False


def print_board():
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
solve(0)
