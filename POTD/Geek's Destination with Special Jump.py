
# Geek starts at position 0 on the positive X-axis and needs to reach or pass position d on the positive X-axis.

# Geek normally follows a repeating movement pattern:

# Move forward by a units, taking a seconds.
# Move backward by b units, taking b seconds.
# Geek also has a special jump that moves him exactly j units forward in 1 second. He can use it at any time, even in the middle of a forward or backward movement, and the journey ends immediately after the jump.

# Given five integers a, b, d, l, and r. For every integer j in the range[l, r], find the minimum time required for Geek to reach or pass position d. He may either use the special jump or reach the destination using normal movement alone, whichever takes less time.

# Return the sum of the minimum times for all jump lengths from l to r. Since, the answer can be large, return modulo 109 + 7.

# Note: Each jump length is considered independently.


# Prefix Sum - O(1) Time and O(1) Space
# Returns the minimum time for a fixed jump length.
def solve(a, b, c, d):
    remaining = d - c

    if remaining <= 0:
        return 1

    if remaining <= a:
        return remaining + 1

    net = a - b
    distance = remaining - a
    cycles = (distance + net - 1) // net

    return remaining + 2 * b * cycles + 1


# Returns the sum of all missing intervals up to t.
def summ(a, b, t):
    MOD = 1000000007
    first = a + 2
    cycleTime = a + b

    if t < first:
        return 0

    count = (t - first) // cycleTime + 1
    last = first + (count - 1) * cycleTime

    term1 = (b % MOD) * (count % MOD) % MOD
    term1 = term1 * ((first + last) % MOD) % MOD

    term2 = (count % MOD) * (2 * b - 1) % MOD
    term2 = term2 * (2 * b) % MOD
    term2 = term2 * ((MOD + 1) // 2) % MOD

    return (term1 + term2) % MOD


# Returns the prefix sum of all possible times up to t.
def prefix(a, b, t):
    MOD = 1000000007

    total = (t % MOD) * ((t + 1) % MOD) % MOD
    total = total * ((MOD + 1) // 2) % MOD

    return (total - summ(a, b, t) + MOD) % MOD


# Calculates the sum of minimum times for all jump lengths.
def minTime(a, b, d, l, r):
    MOD = 1000000007

    t1 = solve(a, b, l, d)
    t2 = solve(a, b, r + 1, d)

    return (prefix(a, b, t1) - prefix(a, b, t2) + MOD) % MOD


# Driver Code
if __name__ == "__main__":
    a, b, d, l, r = 2, 1, 5, 3, 4

    print(minTime(a, b, d, l, r))
