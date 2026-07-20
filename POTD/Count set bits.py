import math


def countSetBits(n):
    # Base case
    if n == 0:
        return 0

    # Find highest power of 2 less than or equal to n
    x = int(math.log2(n))

    # Special case to avoid shifting negative
    if x == 0:
        return 1   # because set bits from 1 → 1

    # Set bits in full patterns from 0 to (2^x - 1)
    fullBits = x * (1 << (x - 1))
    

    # Contribution of MSB from 2^x to n
    msbBits = n - (1 << x) + 1
    # Recursively handle remaining part
    remaining = n - (1 << x)
    remainingBits = countSetBits(remaining)
    

    return fullBits + msbBits + remainingBits


if __name__ == "__main__":
    n = 11
    print(countSetBits(n))
