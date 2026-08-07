# Given n friends, each one can remain single or can be paired up with some other friend. Each friend can be paired only once. Find out the total number of ways in which friends can remain single or can be paired up

# Using Space Optimized DP (Fibonacci Style) - O(n) Time O(1) Space


def countFriendsPairings(n: int) -> int:
    a, b, c = 1, 2, 0

    # handling base cases
    if n <= 2:
        return n

    # iterating from 3 to n
    for i in range(3, n + 1):

        # applying recurrence relation:
        # f(i) = f(i-1) + (i-1) * f(i-2)
        c = b + (i - 1) * a

        # updating previous two values
        a = b
        b = c

    return c
    

n = 15
print(countFriendsPairings(n))
