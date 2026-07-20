# def check(start, end, s, n):
#     print("check", start, end, n)
#     if end > n:
#         return False
#     while 0 <= start <= end and end <= n:
#         if s[start] == s[end]:
#             print("barabar")
#             return check(start + 1, end - 1, s, n)
#         else:
#             print("else")
#             return check(start, end + 1, s, n)
#
#     return True
#
#
#
#
# def palinSub(s):
#     n = len(s)
#     palin = 0
#
#     for i in range(0, n - 1):
#         print("i", i)
#         if check(i, i + 1, s, n):
#             print("ziad")
#             palin += 1
#
#     return palin





# [Better Approach 2] Using Bottom-Up DP (Tabulation) - O(n^2) Time and O(n^2) Space---------------------------------------------------------------------------------------------

# def countPalinSub(s):
#     n = len(s)
#     dp = [[False for _ in range(n)] for _ in range(n)]
#     res = 0
#
#     for i in range(n):
#         dp[i][i] = True
#         if i < n - 1:
#             if s[i] == s[i + 1]:
#                 dp[i][i + 1] = True
#                 res += 1
#
#     print(dp, res)
#
#     for gap in range(2, n):
#         for i in range(n - gap):
#             j = i + gap
#             if s[i] == s[j] and dp[i + 1][j - 1]:
#                 dp[i][j] = True
#                 res += 1
#
#     return res
#--------------------------------------------------------------------------------------
# def countPalindromes(s):

#     n = len(s)
#     count = 0

#     # Count odd length palindrome substrings
#     # with str[i] as center.
#     for i in range(len(s)):
#         left = i - 1
#         right = i + 1
#         while left >= 0 and right < n:
#             if s[left] == s[right]:
#                 count += 1
#             else:
#                 break
#             left -= 1
#             right += 1

#     for i in range(len(s)):
#         left = i
#         right = i + 1
#         while left >= 0 and right < n:
#             if s[left] == s[right]:
#                 count += 1
#             else:
#                 break
#             left -= 1
#             right += 1

#     return count



# s = "abbaeae"
# print(countPalinSub(s))


# [Better Approach 1] Using Memoization - O(n^2) Time and O(n^2) Space----------------------------------------

# Python program to count all palindromic substrings of
# a given string using memoization

def isPalindrome(i, j, s, memo):

    # One length string is always palindrome
    if i == j:
        return 1

    # Two length string is palindrome if
    # both characters are same
    if j == i + 1 and s[i] == s[j]:
        return 1

    # if current substring is already checked
    if memo[i][j] != -1:
        return memo[i][j]

    # Check if the characters at i and j are equal
    # and the substring inside is palindrome
    if s[i] == s[j] and isPalindrome(i + 1, j - 1, s, memo) == 1:
        memo[i][j] = 1
    else:
        memo[i][j] = 0

    return memo[i][j]


def countPS(s):
    n = len(s)

    # Memoization table
    memo = [[-1 for i in range(n)] for i in range(n)]

    res = 0
    for i in range(n):
        for j in range(i + 1, n):

            # Check if the substring is palindrome
            if isPalindrome(i, j, s, memo) == 1:
                res += 1

    return res


if __name__ == "__main__":
    s = "abaab"
    print(countPS(s))
