import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


def max_lcm(n):
    if n <= 2:
        return n
    if n % 2 != 0:
        return lcm(n, lcm(n-1, n-2))
    elif n % 3 != 0:
        return lcm(n, lcm(n-1, n-3))
    else:
        return lcm(n-1, lcm(n-2, n-3))


n = 987
print(max_lcm(n))
# 958584270

# [Naive Approach] Triple Nested LCM Check - O(n^3 log(n)) Time and O(1) Space----------------------------------------
# Function to compute GCD (Greatest Common Divisor)
# # using Euclidean Algorithm
# def gcd(a, b):
#     if a == 0:
#         return b
#     return gcd(b % a, a)

# # Function to compute LCM
# # (Least Common Multiple) of two numbers


# def lcm(a, b):
#     product = a * b
#     return product // gcd(a, b)

# # Function to compute the maximum LCM among all triplets
# # (i, j, k) such that 1 <= i <= j <= k <= n


# def lcmTriplets(n):
#     maxLCM = 1

#     # Iterate over all combinations of triplets (i, j, k)
#     for i in range(1, n + 1):
#         for j in range(i, n + 1):
#             for k in range(j, n + 1):

#                 # Calculate LCM of the triplet and update maximum
#                 currentLCM = lcm(lcm(i, j), k)
#                 maxLCM = max(maxLCM, currentLCM)

#     return maxLCM


# if __name__ == "__main__":
#     n = 9
#     print(lcmTriplets(n))


# Time Complexity: O(log(min(a, b))), where a and b are two parameters of gcd.------------------------------------------------
# Auxiliary Space: O(log(min(a, b)))

# def lcmTriplets(n):
#     if n < 3:

#         # Not enough numbers to form a triplet
#         return n

#     if n % 2 != 0:

#         # If n is odd: use n, n-1, n-2
#         return n * (n - 1) * (n - 2)

#     if math.gcd(n, n - 3) == 1:

#         # Even n, but coprime with n-3: use n, n-1, n-3
#         return n * (n - 1) * (n - 3)

#     # Even n and not coprime with n-3: use n-1, n-2, n-3
#     return (n - 1) * (n - 2) * (n - 3)


# if __name__ == "__main__":
#     n = 9
#     print(lcmTriplets(n))

# [Efficient Approach] Pattern-Based Conditional Optimization - O(1) Time and O(1) Space-----------------------------------------

# def lcmTriplets(n):
#     if n < 3:
#         return n

#     # If n is odd, the product of the top 3 numbers gives maximum LCM
#     if n % 2 != 0:
#         return n * (n - 1) * (n - 2)

#     # If n is even and not divisible by 3, use n, n-1, n-3
#     if n % 3 != 0:
#         return n * (n - 1) * (n - 3)

#     # If n is even and divisible by 3, use n-1, n-2, n-3
#     return (n - 1) * (n - 2) * (n - 3)


# if __name__ == "__main__":
#     n = 9
#     print(lcmTriplets(n))
print(bin(123))
