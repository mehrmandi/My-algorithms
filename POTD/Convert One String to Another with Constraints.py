# Given two strings s1 and s2, consisting only of the characters 'A', 'B', and '#'. Determine whether s1 can be transformed into s2 by performing the following operations on s1:

# 'A' can move only towards the left.
# 'B' can move only towards the right.
# Neither 'A' nor 'B' can cross each other.
# '#' represents an empty position through which 'A' and 'B' can move.
# Moving the character at index i one step to the left means swapping it with the character at index i - 1, provided i - 1 >= 0. Similarly, moving it one step to the right means swapping it with the character at index i + 1, provided i + 1 < s1.length().

# Return true if s1 can be transformed into s2
# otherwise, return false.

# Two-Pointer Walk Over Non-'#' Characters - O(n + m) Time and O(1) Space

def isItPossible(s1, s2):
    m, n = len(s1), len(s2)

    if m != n:
        return False

    i, j = 0, 0

    while i < m or j < n:

        # skip '#' characters in both strings
        while i < m and s1[i] == '#':
            i += 1
        while j < n and s2[j] == '#':
            j += 1

        # both strings have ended: every character matched successfully
        if i >= m and j >= n:
            break

        # only one string has ended: the counts of non-'#' characters differ
        if i >= m or j >= n:
            return False

        # characters must match in identity and relative sequence order
        if s1[i] != s2[j]:
            return False

        # 'A' can only move left, so its s2 position must not exceed its s1 position
        if s1[i] == 'A' and i < j:
            return False

        # 'B' can only move right, so its s2 position must not be less than its s1 position
        if s1[i] == 'B' and i > j:
            return False

        i += 1
        j += 1

    return True


s1 = "#A#B#B#"
s2 = "A###B#B"
print(isItPossible(s1, s2))
