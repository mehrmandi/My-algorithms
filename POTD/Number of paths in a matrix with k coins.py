
# def numberOfPath(mat, k):
#     n = len(mat)
#     m = len(mat[0])
#     res = 0
#     q = [[0, 0, mat[0][0]]]
    
#     directions = [[0, 1], [1, 0]]
    
#     while q:
#         x, y, sum = q.pop()
        
#         for dir in directions:
#             newX = x + dir[0]
#             newY = y + dir[1]
            
#             if newX == n - 1 and newY == m - 1 and sum + mat[newX][newY] == k:
#                 res += 1
            
#             if newX < n and newY < m:
#                 q.append([newX, newY, sum + mat[newX][newY]])

#     return res
    
    

# k = 16
# mat = [[1, 2, 3], 
#                       [4, 6, 5], 
#                       [9, 8, 7]]


# print(numberOfPath(mat, k))

def numberOfPath(mat, k):
    n = len(mat)
    m = len(mat[0])

    # Use only two 2D arrays for space optimization
    prev = [[0] * (k + 1) for _ in range(m)]
    curr = [[0] * (k + 1) for _ in range(m)]
    
    # Build DP table iteratively
    for i in range(n):
        for j in range(m):
            for sum_ in range(k + 1):
                print("i, j, sum_", i, j, sum_)

                # Base case
                if i == 0 and j == 0:
                    print("1111111111")
                    # Only one way if sum matches cell value
                    curr[j][sum_] = 1 if sum_ == mat[0][0] else 0
                    print(curr[j][sum_])
                    continue

                curr[j][sum_] = 0
                print(prev)
                print(curr)

                if sum_ - mat[i][j] >= 0:
                    print("22222222222")
                    # from top
                    if i > 0:
                        print("iiiiii", curr[j][sum_], prev[j][sum_ - mat[i][j]])
                        curr[j][sum_] += prev[j][sum_ - mat[i][j]]
                        print("iiiiii", curr[j][sum_])
                    # from left
                    if j > 0:
                        print("jjjjjjjjj", curr[j][sum_],
                              curr[j - 1][sum_ - mat[i][j]])
                        curr[j][sum_] += curr[j - 1][sum_ - mat[i][j]]
        print("ja bedeee", curr)
        # Move current row to previous row
        prev = [row[:] for row in curr]

    # Total ways to reach bottom-right with sum = k
    return prev[m - 1][k]


mat = [[1, 2, 3],
         [4, 6, 5],
         [3, 2, 1]]

k = 12

print(numberOfPath(mat, k))
