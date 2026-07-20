# [Approach -1] Using Recursion + Backtracking - O(8n*n) Time and O(n2) Space



# dx = [-2, -2, 2, 2, -1, -1, 1, 1]
# dy = [-1, 1, -1, 1, -2, 2, -2, 2]

# def isValid(nX, nY, board, n):
#     return nX >= 0 and nY >= 0 and nX < n and nY < n and board[nX][nY] == -1

# def stepFindRec(board, X, Y, step, n):
#     if step == n * n:
#         return True
    
#     for i in range(8):
#         nX, nY = X + dx[i], Y + dy[i]
        
#         if isValid(nX, nY, board, n):
#             board[nX][nY] = step
            
#             if stepFindRec(board, nX, nY, step + 1, n):
#                 return True
            
#             board[nX][nY] = -1
            
#     return False
            

# def knightTour(n):
#     board = [[-1 for _ in range(n)] for _ in range(n)]
    
#     board[0][0] = 0

#     if stepFindRec(board, 0, 0, 1, n):
#         return board
    
#     return [[-1]]
    
    
# n = 5
# print(knightTour(n))






# # [Approach -2] Using Warnsdorff's Algorithm - O(n3) Time and O(n2) Space----------------------------------------
# # Define 8 knight moves globally
# dir = [
#     [2, 1], [1, 2], [-1, 2], [-2, 1],
#     [-2, -1], [-1, -2], [1, -2], [2, -1]
# ]

# # Count the number of onward moves from position (x, y)


# def countOptions(board, x, y):
#     count, n = 0, len(board)
#     for dx, dy in dir:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
#             count += 1
#     return count

# # Generate valid knight moves from (x, y), sorted by fewest onward moves


# def getSortedMoves(board, x, y):
#     moveList, n = [], len(board)
#     for i in range(8):
#         nx, ny = x + dir[i][0], y + dir[i][1]
#         if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
#             options = countOptions(board, nx, ny)
#             moveList.append([options, i])
#     moveList.sort()
#     return moveList

# # Recursive function to solve the Knight's Tour


# def knightTourUtil(x, y, step, n, board):
#     if step == n * n:
#         return True
#     moves = getSortedMoves(board, x, y)
#     for move in moves:
#         dirIdx = move[1]
#         nx, ny = x + dir[dirIdx][0], y + dir[dirIdx][1]
#         board[nx][ny] = step
#         if knightTourUtil(nx, ny, step + 1, n, board):
#             return True

#         # Backtrack
#         board[nx][ny] = -1
#     return False

# # Function to start Knight's Tour


# def knightTour(n):
#     board = [[-1]*n for _ in range(n)]
#     board[0][0] = 0
#     if knightTourUtil(0, 0, 1, n, board):
#         return board
#     return [[-1]]


# if __name__ == '__main__':
#     n = 2
#     result = knightTour(n)
#     for row in result:
#         print(*row)
        
# # [Approach -2] Using Warnsdorff's Algorithm - O(n3) Time and O(n2) Space----------------------------------------
def knights_tour(n):
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]

    board = [[-1 for _ in range(n)] for _ in range(n)]
    board[0][0] = 0  # Start at top-left corner

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1

    def count_onward_moves(x, y):
        return sum(1 for dx, dy in moves if is_valid(x + dx, y + dy))

    def next_move(x, y):
        candidates = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            print(nx, ny, x, y)
            if is_valid(nx, ny):
                print("count", (count_onward_moves(nx, ny), nx, ny))
                candidates.append((count_onward_moves(nx, ny), nx, ny))
        candidates.sort()
        return [(nx, ny) for _, nx, ny in candidates]

    def tour(x, y, step):
        if step == n * n:
            return True
        print("move", next_move(x, y))
        for nx, ny in next_move(x, y):
            board[nx][ny] = step
            if tour(nx, ny, step + 1):
                return True
            board[nx][ny] = -1  # Backtrack
        return False

    if tour(0, 0, 1):
        return board
    else:
        return []


# Example usage:
n = 5
result = knights_tour(n)
if result:
    for row in result:
        print(row)
else:
    print("No solution found.")
