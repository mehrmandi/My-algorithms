# [Expected Approach] Using Space Optimization - O(n*m*k) Time and O(m*k) Space------------------------



def chocolatePickup(mat):
    n = len(mat)
    

    # for storing the answers for current row
    curr = [[0] * n for _ in range(n)]

    # for storing the answers of next row
    next = [[0] * n for _ in range(n)]

    # filling dp array in bottom up way
    for i1 in range(n - 1, -1, -1):

        # creating a new array to fill answers
        # for current row based on next row
        curr = [[0] * n for _ in range(n)]

        for j1 in range(n - 1, -1, -1):
            for j2 in range(n - 1, -1, -1):

                # base case
                if i1 == n - 1 and j1 == n - 1 and j2 == n - 1:
                    curr[n - 1][n - 1] = (-1 if mat[n - 1]
                                          [n - 1] == -1 else mat[n - 1][n - 1])
                    continue

                i2 = i1 + j1 - j2

                # robot2 in an invalid row
                if i2 >= n or i2 < 0:
                    continue
                ans = -1
                dir = [[1, 0], [0, 1]]
                for d1 in dir:
                    for d2 in dir:
                        newRow1 = i1 + d1[0]
                        newCol1 = j1 + d1[1]
                        newRow2 = i2 + d2[0]
                        newCol2 = j2 + d2[1]

                        # taking maximum chocolates
                        # among all possibilities
                        if (newRow1 < n and newRow2 < n and newCol1 < n and newCol2 < n
                                and mat[newRow1][newCol1] != -1 and mat[newRow2][newCol2] != -1):
                            if newRow1 == i1 + 1:
                                ans = max(ans, next[newCol1][newCol2])
                            else:
                                ans = max(ans, curr[newCol1][newCol2])

                if ans == -1 or mat[i1][j1] == -1 or mat[i2][j2] == -1:
                    curr[j1][j2] = -1
                    continue
                ans += mat[i1][j1]

                # if both robots not in the same cell
                if i1 != i2 and mat[i1][j1] != -1:
                    ans += mat[i2][j2]
                curr[j1][j2] = ans
        next = curr

    # returning 0 if its not possible(negative value)
    # else maximum chocolates obtained
    return max(0, next[0][0])


if __name__ == "__main__":
    mat = [
        [0, 1, -1],
        [1, 1, -1],
        [1, 1, 2]
    ]
    print(chocolatePickup(mat))
