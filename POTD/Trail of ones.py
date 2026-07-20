# [Optimized Approach] Using nth Fibonacci - O(2 ^ n) Time and O(n) Space ----------------------------------


# def nonPair(n):
#     if n == 2:
#         return 3

#     if n == 3:
#         return 5

    
#     else:
#         return nonPair(n - 1) + nonPair(n - 2)
    
    
# def trailOnes(n):
#     return (2 ** n) - nonPair(n)


# n = 37
# print(trailOnes(n))

# [Naive Approach] Using Recursion - O(2n) Time and O(n) Space----------------------------------

# Recursive helper to count numbers with
# at least one pair of consecutive 1s
# def solve(i, prev, n):
#     if i > n:
#         return 0

#     if prev == 0:
#         # Try placing 1 or 0 at the current position
#         return solve(i + 1, 1, n) + \
#             solve(i + 1, 0, n)
#     else:
#         # try placing 0 after a 1
#         res = solve(i + 1, 0, n)
#         # try placing 1: now remaining positions can be anything
#         # atleast 1 time consecutive '1' is found
#         res += 1 << (n-i)
#         return res


# def countConsec(n):
#     return solve(1, 0, n)


# if __name__ == "__main__":
#     n = 3
#     print(countConsec(n))

# [Optimized Approach] Using nth Fibonacci - O(log(n)) Time and O(log(n)) Space
# Function to multiply two 2x2 matrices
# Time Complexity: O(n) since there are only 2 choices for prev and n positions, the total number of unique subproblems is 2 * n.------------------------
# Auxiliary Space: O(n) due to recursion stack in the worst case and the dp table of size 2 * (n+1) used for memoization.---------------------------------

# Recursive helper to count numbers with
# at least one pair of consecutive 1s
# def solve(i, prev, n, dp):
#     if i > n:
#         return 0

#     if dp[i][prev] != -1:
#         return dp[i][prev]

#     res = 0

#     if prev == 0:
#         # try placing '1' or '0' at the current position
#         res = solve(i + 1, 1, n, dp) + \
#             solve(i + 1, 0, n, dp)
#     else:
#         # try placing '0' after a '1'
#         res = solve(i + 1, 0, n, dp)

#         # try placing '1': now remaining positions can be anything
#         # at least 1 time consecutive '1' is found
#         res += 1 << (n-i)

#     dp[i][prev] = res
#     return res


# def countConsec(n):
#     dp = [[-1] * 2 for _ in range(n + 2)]
#     return solve(1, 0, n, dp)


# if __name__ == "__main__":
#     n = 3
#     print(countConsec(n))


# [Better Approach 2] Bottom-Up Dynamic Programming - O(n) Time and O(n) Space

# def countConsec(n):
#     # dp[i][prev] = number of binary strings from index i to n
#     # with previous bit 'prev' and at least one pair of consecutive '1's
#     dp = [[0] * 2 for _ in range(n + 2)]

#     # iterate from i = n to 1
#     for i in range(n, 0, -1):
#         for prev in range(2):
#             if prev == 0:
#                 # place '0' or '1'
#                 dp[i][prev] = dp[i + 1][0] + dp[i + 1][1]
#             else:
#                 # place '0' after '1'
#                 dp[i][prev] = dp[i + 1][0]

#                 # place '1' after '1' → found one pair of consecutive '1's,
#                 # rest (n - i) bits can be anything: 2^(n - i)
#                 dp[i][prev] += (1 << (n - i))

#     # start from index 1, with prev = 0
#     return dp[1][0]


# if __name__ == "__main__":
#     n = 3
#     print(countConsec(n))


# [Expected Approach 1] Space-Optimized Bottom-Up Dynamic Programming - O(n) Time and O(1) Space-------------------------------------
# def countConsec(n):
#     prev0, prev1 = 0, 0

#     for i in range(n, 0, -1):
#         # if previous bit is 0, we can place 0 or 1
#         curr0 = prev0 + prev1

#         # if previous bit is 1, placing another 1 creates a valid pair,
#         # remaining bits can be anything: 2^(n - i)
#         curr1 = prev0 + (1 << (n - i))

#         # update for next round
#         prev0, prev1 = curr0, curr1

#     # start from position 1 with previous bit 0
#     return prev0


# if __name__ == "__main__":
#     n = 3
#     print(countConsec(n))


# [Expected Approach 2] Complement Counting using Dynamic Programming - O(n) Time and O(1) Space----------------------------
# def countConsec(n):
#     # prev0 -> number of strings of length i ending
#     # in '0' with no consecutive 1s

#     # prev1 -> number of strings of length i ending
#     # in '1' with no consecutive 1s
#     prev0, prev1 = 1, 1

#     for i in range(2, n + 1):
#         # if we add '0', it can follow both '0' and '1'
#         curr0 = prev0 + prev1

#         # if we add '1', it can only follow '0'
#         curr1 = prev0

#         prev0, prev1 = curr0, curr1

#     total = 1 << n
#     noConsec = prev0 + prev1
#     consec = total - noConsec
#     return consec


# if __name__ == "__main__":
#     n = 3
#     print(countConsec(n))
def multiply(mat1, mat2):

    # Perform matrix multiplication
    x = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    y = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    z = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
    w = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]

    # Update matrix mat1 with the result
    mat1[0][0] = x
    mat1[0][1] = y
    mat1[1][0] = z
    mat1[1][1] = w

# Function to perform matrix exponentiation


def matrixPower(mat1, n):

    # Base case for recursion
    if n == 0 or n == 1:
        return

    # Initialize a helper matrix
    mat2 = [[1, 1], [1, 0]]

    # Recursively calculate mat1^(n/2)
    matrixPower(mat1, n // 2)

    # Square the matrix mat1
    multiply(mat1, mat1)

    # If n is odd, multiply by the helper matrix mat2
    if n % 2 != 0:
        multiply(mat1, mat2)

# Function to calculate the nth Fibonacci number
# using matrix exponentiation


def nthFibonacci(n):
    if n <= 1:
        return n

    mat1 = [[1, 1], [1, 0]]

    # Raise the matrix mat1 to the power of (n - 1)
    matrixPower(mat1, n - 1)

    return mat1[0][0]

# Function to count binary strings of length n
# that have at least one pair of consecutive 1's


def countConsec(n):
    # Total binary strings of length n = 2^n
    total = 1 << n
    # Count of strings without consecutive 1's = Fib(n + 2)
    noConsec = nthFibonacci(n + 2)
    return total - noConsec


if __name__ == "__main__":
    n = 37
    print(countConsec(n))
    
    
    

