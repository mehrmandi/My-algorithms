# Given a binary matrix mat[][] of size n x m, find the maximum area of a rectangle containing only 1s. You are allowed to swap any columns of the matrix any number of times before forming the rectangle. Return the maximum possible rectangle area.

# Counting Sort on Heights - O(n * (n + m)) Time and O(n * m) Space

def maxArea(mat: list[list[int]]) -> int:
    n = len(mat)
    m = len(mat[0])

    height = [[0] * m for _ in range(n)]

    # height[i][j] stores consecutive 1s ending at row i in column j.
    for j in range(m):
        height[0][j] = mat[0][j]

        for i in range(1, n):
            if mat[i][j] == 1:
                height[i][j] = height[i - 1][j] + 1

    ans = 0

    for i in range(n):
        count = [0] * (n + 1)

        # Count frequency of each height.
        for j in range(m):
            count[height[i][j]] += 1

        col = 0


        # Rearrange heights in decreasing order using counting sort.
        for h in range(n, -1, -1):
            while count[h] > 0:
                height[i][col] = h
                col += 1
                count[h] -= 1

        # Calculate maximum area for this row.
        for j in range(m):
            ans = max(ans, height[i][j] * (j + 1))

    return ans


mat = [
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1]
]
print(maxArea(mat))
