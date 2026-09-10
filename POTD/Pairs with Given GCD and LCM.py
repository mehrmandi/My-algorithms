# Given two integers x and y representing the GCD and LCM respectively of two unknown positive integers a and b, count the number of valid pairs(a, b) satisfying these conditions. Note that(a, b) and (b, a) are counted as distinct pairs when a ≠ b.

# Find Coprime Factor Pairs - O(√(y/x) log(y/x)) Time and O(1) Space

from math import gcd, sqrt


def pairCount(x, y):
    n = 0
    res = 0

    # lcm must be divisible by gcd, else no pair exists
    if y % x == 0:
        n = y // x

    # if n is 1, the only pair is (x, x)
    if n == 1:
        res = 1

    # find coprime factor pairs (i, n/i) of n
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            j = n // i

            # both (x*i, x*j) and (x*j, x*i) are valid
            # only if i and j are coprime (gcd = 1)
            if i != j and gcd(x * i, x * j) == x:
                res += 2

    return res
