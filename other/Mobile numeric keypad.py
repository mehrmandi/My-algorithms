def count_sequences(n):
    if n <= 0:
        return 0

    # Allowed moves for each digit.
    neighbors = {
        1: [1, 2, 4],
        2: [2, 1, 3, 5],
        3: [3, 2, 6],
        4: [4, 1, 5, 7],
        5: [5, 2, 4, 6, 8],
        6: [6, 3, 5, 9],
        7: [7, 4, 8],
        8: [8, 5, 7, 9, 0],
        9: [9, 6, 8],
        0: [0, 8]
    }

    # Initialize dp for sequences of length 1: one way for each digit.
    dp = [1] * 10  # dp[digit] holds count for sequences ending on that digit

    # Build sequences from length 2 up to n.
    for _ in range(2, n + 1):
        next_dp = [0] * 10
        for digit in range(10):
            for next_digit in neighbors[digit]:
                next_dp[next_digit] += dp[digit]
        dp = next_dp

    return sum(dp)


# Example usage:
n = 5
print("Number of unique sequences of length", n, ":", count_sequences(n))
