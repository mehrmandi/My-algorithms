# def evaluate(b1, b2, op):
#     if op == '&':
#         return b1 & b2
#     elif op == '|':
#         return b1 | b2
#     return b1 ^ b2
#
# def countRecur(i, j, req, s, memo):
#
#     # Base case:
#     if i == j:
#         return 1 if req == (1 if s[i] == 'T' else 0) else 0
#
#     # If value is memoized
#     if memo[i][j][req] != -1:
#         return memo[i][j][req]
#
#     ans = 0
#     for k in range(i + 1, j, 2):
#
#         # Count Ways in which left substring
#         # evaluates to true and false.
#         left_true = countRecur(i, k - 1, 1, s, memo)
#         left_false = countRecur(i, k - 1, 0, s, memo)
#
#         # Count Ways in which right substring
#         # evaluates to true and false.
#         right_true = countRecur(k + 1, j, 1, s, memo)
#         right_false = countRecur(k + 1, j, 0, s, memo)
#
#         # Check if the combinations result
#         # to req.
#         if evaluate(1, 1, s[k]) == req:
#             ans += left_true * right_true
#         if evaluate(1, 0, s[k]) == req:
#             ans += left_true * right_false
#         if evaluate(0, 1, s[k]) == req:
#             ans += left_false * right_true
#         if evaluate(0, 0, s[k]) == req:
#             ans += left_false * right_false
#
#     memo[i][j][req] = ans
#     return ans
#
# def countWays(s):
#
#     n = len(s)
#     memo = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]
#     return countRecur(0, n - 1, 1, s, memo)


#--------------------------------------------------------------------------------------------------

def evaluate(b1, b2, op):
    if op == '&':
        return b1 & b2
    if op == '|':
        return b1 | b2
    return b1 ^ b2


def countWays(s):
    n = len(s)
    dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

    # Base case: Single operands (T or F)
    for i in range(0, n, 2):
        dp[i][i][1] = 1 if s[i] == 'T' else 0
        dp[i][i][0] = 1 if s[i] == 'F' else 0

    # Iterate over different substring lengths
    for length in range(2, n, 2):  # length increases by 2 (odd indices are operators)
        for i in range(0, n - length, 2):
            j = i + length
            # Reset values for the current subproblem
            dp[i][j][0] = dp[i][j][1] = 0

            for k in range(i + 1, j, 2):  # Iterate over operators
                op = s[k]
                leftTrue, leftFalse = dp[i][k - 1][1], dp[i][k - 1][0]
                rightTrue, rightFalse = dp[k + 1][j][1], dp[k + 1][j][0]

                # Count ways to get True or False
                if evaluate(1, 1, op):
                    dp[i][j][1] += leftTrue * rightTrue
                if evaluate(1, 0, op):
                    dp[i][j][1] += leftTrue * rightFalse
                if evaluate(0, 1, op):
                    dp[i][j][1] += leftFalse * rightTrue
                if evaluate(0, 0, op):
                    dp[i][j][1] += leftFalse * rightFalse

                if not evaluate(1, 1, op):
                    dp[i][j][0] += leftTrue * rightTrue
                if not evaluate(1, 0, op):
                    dp[i][j][0] += leftTrue * rightFalse
                if not evaluate(0, 1, op):
                    dp[i][j][0] += leftFalse * rightTrue
                if not evaluate(0, 0, op):
                    dp[i][j][0] += leftFalse * rightFalse

    return dp[0][n - 1][1]  # Return ways to make entire expression True





s = "T|T&F^T"
print(countWays(s))