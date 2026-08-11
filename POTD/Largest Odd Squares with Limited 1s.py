# Given a binary matrix mat[][] of size n*m and an integer k, process a list of queries queries[][]. Each query contains coordinates[i, j] of the center of a square.

# For every query, find the side length of the largest odd-sized square centered at cell(i, j) such that the square contains at most k ones.
# A square centered at(i, j) expands outward symmetrically in all four directions by the same number of cells, so its side length is always odd.
# Note: If no odd-sized square centered at the given cell satisfies the condition of containing at most k ones, return -1 for that query.


# Using 2D Prefix Sum and Binary Search

# Time Complexity: O(n * m + q * log(min(n, m))), O(n * m) to build the 2D prefix sum, and each query takes O(log(min(n, m))) due to binary search with O(1) square-sum calculation.
# Auxiliary Space: O(n * m), for the 2D prefix sum array.


def largestSquare(mat: list[list[int]], queries: list[list[int]], k: int) -> list[int]:
    res = []
    n = len(mat)
    m = len(mat[0])

    # Build suffix sum
    suf = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            suf[i + 1][j + 1] = suf[i][j + 1] + suf[i + 1][j] - \
                suf[i][j] + mat[i][j]
                
    
    # Process each query
    for q in queries:
        r, c = q
        lo, hi = 0, min(r, c, n - r - 1, m - c - 1)
        max_size = 0
        
        if mat[r][c] > k:
            res.append(-1)
            continue
        
        
        while lo <= hi:
            mid = (lo + hi) // 2
            # Calculate the total number of ones in the square of side length 2*mid + 1 centered at (r, c)
            total = suf[r + mid + 1][c + mid + 1] - suf[r - mid][c + mid + 1] - suf[r + mid + 1][c - mid] + suf[r - mid][c - mid]

            if total <= k:
                max_size = mid
                lo = mid + 1
            else:
                hi = mid - 1
                
        res.append(2 * max_size + 1)
        
    return res
        
        
mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
queries = [[1, 1], [2, 2]]
k = 9
print(largestSquare(mat, queries, k))
