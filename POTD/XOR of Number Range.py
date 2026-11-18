# Given two integers l and r, find the bitwise XOR of all integers in the range[l, r](both inclusive).


# XOR Pattern - O(1) Time and O(1) Space

# Function to compute cumulative XOR sum from 1 to n in O(1)
def computeXOR(n: int) -> int:
    # Remainder determines the cycle position
    rem = n % 4

    # If n is a multiple of 4, the XOR sum equals n
    if rem == 0:
        return n

    # If n leaves remainder 1, all preceding pairs cancel out, leaving 1
    if rem == 1:
        return 1

    # If n leaves remainder 2, the XOR sum evaluates to n + 1
    if rem == 2:
        return n + 1

    # If n leaves remainder 3, all numbers fully cancel out to 0
    return 0


# Function to find XOR of elements in range [l, r]
def findXOR(l: int, r: int) -> int:
    # Compute cumulative XOR from 1 up to r
    xor_r = computeXOR(r)

    # Compute cumulative XOR from 1 up to l - 1
    xor_l_minus_1 = computeXOR(l - 1)

    # Cancel out elements from 1 to l - 1 using x ^ x = 0 to get range [l, r]
    return xor_r ^ xor_l_minus_1


# Driver code
if __name__ == "__main__":
    l = 4
    r = 8

    print(findXOR(l, r))