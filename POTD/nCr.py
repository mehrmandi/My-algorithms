import math
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def nCr(n, r):
    if n < r :
        return 0
    
    if  n == r:
        return 1
        
    nFac = factorial(n)
    rFac = factorial(r)
    nRFac = factorial(n - r)
    
    return nFac/(rFac * nRFac)


n = 2
r = 4
print(nCr(n, r))


# [Alternate Approach] Using Logarithmic Formula - O(r) Time and O(1)

# Calculates the binomial coefficient nCr using the logarithmic formula

# def nCr(n, r):

#     # If r is greater than n, return 0
#     if r > n:
#         return 0

#     # If r is 0 or equal to n, return 1
#     if r == 0 or n == r:
#         return 1

#     # Initialize the logarithmic sum to 0
#     res = 0

#     # Calculate the logarithmic sum of the numerator and denominator using loop
#     for i in range(r):

#         # Add the logarithm of (n-i) and subtract the logarithm of (i+1)
#         res += math.log(n-i) - math.log(i+1)

#     # Convert logarithmic sum back to a normal number
#     return round(math.exp(res))


# if __name__ == "__main__":
#     n = 5
#     r = 2
#     print(nCr(n, r))


#----------------------------------------------------------------------------------------------
# [Expected Approach] By using Binomial Coefficient formula - O(r) Time and O(1) Space


# def nCr(n, r):

#     sum = 1

#     # Calculate the value of n choose r
#     # using the binomial coefficient formula
#     for i in range(1, r+1):
#         sum = sum * (n - r + i) // i

#     return sum


# if __name__ == "__main__":
#     n = 5
#     r = 2

#     print(nCr(n, r))
