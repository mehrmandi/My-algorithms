# Given a rectangular paper with dimensions n × m, find the minimum number of squares that can be formed by cutting the paper.  Each cut must be made completely across the remaining paper, either horizontally or vertically.

# Optimized Euclidean Algorithm - O(log(min(n, m))) Time and O(1)

def minSquares(n, m):
    res = 0

   # Continue until the rectangle becomes empty.
    while n > 0 and m > 0:

        # Make n the larger dimension.
        if n < m:
            n, m = m, n

        # Count all possible squares of size m x m.
        res += n // m

        # Keep the remaining rectangle.
        n %= m

    return res


n = 2
m = 4

print(minSquares(n, m))