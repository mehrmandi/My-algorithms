# Given a non-negative integer n, you can only change a set bit(1) to an unset bit(0). Find the maximum possible value of n such that its binary representation does not contain three consecutive set bits(111) after performing zero or more allowed operations.

# Dynamic Programming Over Bits - O(log n) Time and O(log n) Space

bits = [0] * 31
dp = [[0] * 3 for _ in range(31)]
vis = [[False] * 3 for _ in range(31)]

# Returns the maximum value using bits from pos down to 0.


def solve(pos, ones):
    if pos < 0:
        return 0

    if vis[pos][ones]:
        return dp[pos][ones]

    vis[pos][ones] = True

    # Option 1: Clear the current bit.
    res = solve(pos - 1, 0)

    # Option 2: Keep the current bit set if allowed.
    if bits[pos] == 1 and ones < 2:
        res = max(res, (1 << pos) + solve(pos - 1, ones + 1))

    dp[pos][ones] = res
    return res


def maxValue(n):
    global bits, dp, vis

    bits = [0] * 31
    dp = [[0] * 3 for _ in range(31)]
    vis = [[False] * 3 for _ in range(31)]

    # Store the binary representation of n.
    for i in range(31):
        bits[i] = (n >> i) & 1

    return solve(30, 0)

n = 7
print(maxValue(n))
