def is_power_of_5(binary_str):
    # Check for leading zeros
    if binary_str[0] == '0':
        return False
    val = int(binary_str, 2)
    if val == 0:
        return False
    # Check if val is a power of 5
    while val % 5 == 0:
        val //= 5
    return val == 1


def minimum_splits(s):
    n = len(s)
    # dp[i] = min cuts needed for s[0:i]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # base case: empty string

    for i in range(1, n + 1):
        for j in range(i):
            substring = s[j:i]
            if is_power_of_5(substring):
                print("hast", dp, i, j)
                dp[i] = min(dp[i], dp[j] + 1)
            print(dp)


    return dp[n] if dp[n] != float('inf') else -1


# Example usage
s = "101101101"
print(minimum_splits(s))  # Output: 3

