# def makeNewMatrix(mat):
#     n = len(mat)
#     m = len(mat[0])
#     new_mat = [[0 for _ in range(m)] for _ in range(n)]
#     new_mat[0] = mat[0]
#
#     for i in range(1, n):
#         for j in range(m):
#             if mat[i][j] == 1:
#                 new_mat[i][j] = mat[i][j] + new_mat[i - 1][j]
#
#     return new_mat
#
#
# def getMaxArea(arr):
#     n = len(arr)
#     s = []
#     res = 0
#
#
#     for i in range(n):
#         while s and arr[s[-1]] >= arr[i]:
#             tp = s.pop()
#             width = i if not s else i - s[-1] - 1
#
#             res = max(res, arr[tp] * width)
#
#         s.append(i)
#
#     while s:
#         tp = s.pop()
#         width = n if not s else n - s[-1] - 1
#         res = max(res, arr[tp] * width)
#
#     return res
#
# def maxRectangle(mat):
#     new_mat = makeNewMatrix(mat)
#     n = len(mat)
#     max_area = 0
#
#     for i in range(n):
#         max_area = max(max_area, getMaxArea(new_mat[i]))
#
#     return max_area

def maxArea(mat):
    n, m = len(mat), len(mat[0])

    # 2D matrix to store the width of 1's
    # ending at each cell.
    memo = [[0] * m for _ in range(n)]
    print(memo)
    ans = 0

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                continue

            # Set width of 1's at (i, j).
            if j == 0:
                memo[i][j] = 1
            else:
                memo[i][j] = 1 + memo[i][j - 1]

            width = memo[i][j]

            # Traverse row by row, update the
            # minimum width and calculate area.
            for k in range(i, -1, -1):
                width = min(width, memo[k][j])
                area = width * (i - k + 1)

                ans = max(ans, area)

    return ans





mat = [[0, 1, 1, 0],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 0, 0]]

print(maxArea(mat))