# Using Sliding Window - O(n^2) Time and O(n) Space


def maximumSum(mat, k):
    n = len(mat)

    # 1D column sum array — O(n) space
    colSum = [0] * n
    res = float('-inf')

    for i in range(n):

        # Update column sums with new row entering and old row leaving window
        for j in range(n):
            print("i, j, colsum", i, j, colSum)
            colSum[j] += mat[i][j]
            if i >= k:
                print("i >= k", mat[i - k][j])
                colSum[j] -= mat[i - k][j]

        # Slide horizontal window of size k over colSum
        if i >= k - 1:
            windowSum = 0
            print("i >= k", i, windowSum)
            for j in range(n):
                windowSum += colSum[j]
                print('j', windowSum)
                if j >= k:
                    windowSum -= colSum[j - k]
                    print("j >= k", windowSum)
                if j >= k - 1:
                    res = max(res, windowSum)
                    print("j >= k - 1", windowSum, res)

    return res


mat = [[1, 2, -1, 4], [-8, -3, 4, 2], [3, 8, 10, -8], [-4, -1, 1, 7]]
print(maximumSum(mat, 3))
        