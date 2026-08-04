def can_place_bishop(board, row, col, n, m, occupied_diagonals1, occupied_diagonals2):
    if board[row][col] == 1:  # obstacle
        return False
    diag1 = row - col
    diag2 = row + col
    if diag1 in occupied_diagonals1 or diag2 in occupied_diagonals2:
        return False
    return True

def place_bishop(board, row, col, n, m, occupied_diagonals1, occupied_diagonals2, count):
    if row >= n:
        return count

    # Move to the next row if we're at the end of the current row
    if col >= m:
        return place_bishop(board, row + 1, 0, n, m, occupied_diagonals1, occupied_diagonals2, count)

    # Option 1: Skip this cell
    max_bishops = place_bishop(board, row, col + 1, n, m, occupied_diagonals1, occupied_diagonals2, count)

    # Option 2: Place a bishop if possible
    if can_place_bishop(board, row, col, n, m, occupied_diagonals1, occupied_diagonals2):
        occupied_diagonals1.add(row - col)
        occupied_diagonals2.add(row + col)
        max_bishops = max(max_bishops, place_bishop(board, row, col + 1, n, m, occupied_diagonals1, occupied_diagonals2, count + 1))
        occupied_diagonals1.remove(row - col)
        occupied_diagonals2.remove(row + col)

    return max_bishops

def max_bishops(n, m, obstacles):
    board = [[0] * m for _ in range(n)]
    for r, c in obstacles:
        board[r][c] = 1  # mark obstacles

    occupied_diagonals1 = set()  # for \ diagonals
    occupied_diagonals2 = set()  # for / diagonals

    return place_bishop(board, 0, 0, n, m, occupied_diagonals1, occupied_diagonals2, 0)

# Example usage:
n = 10
m = 10
obstacles = [(1, 1), (2, 1), (5, 0), (7, 0), (8, 3), (0, 5), (2, 5), (3, 5),
                 (5, 5), (9, 5), (1, 8), (5, 7), (7, 7), (8, 7), (6, 9)]  # Example obstacle positions
result = max_bishops(n, m, obstacles)
print("Maximum bishops that can be placed:", result)
