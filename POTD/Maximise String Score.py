# [Expected Approach 2] Using Iterative Dp - O(n * 26) Time and O(n * 26) Space----------------

def maxScore(s, jumps):
    n = len(s)

    # jumps to the same char
    jumpsList = [(j[0], j[1]) for j in jumps]
    for ch in range(ord('a'), ord('z') + 1):
        jumpsList.append((chr(ch), chr(ch)))

    nxtInd = [[-1] * 26 for _ in range(n)]
    lastInd = [-1] * 26

    # calculate next index of each character from index i
    for i in range(n - 1, -1, -1):
        for j in range(26):
            nxtInd[i][j] = lastInd[j]
        lastInd[ord(s[i]) - 97] = i

    child = [[] for _ in range(26)]

    # fill child array
    for u, v in jumpsList:
        child[ord(u) - 97].append(v)

    preScore = [0] * (n + 1)

    # computing prefix sum of ASCII values
    for i in range(len(s)):
        preScore[i + 1] = preScore[i] + ord(s[i])

    dp = [0] * n

    for ind in range(n - 2, -1, -1):
        score = 0

        # iterate through every possible character
        for it in child[ord(s[ind]) - 97]:

            jmpInd = nxtInd[ind][ord(it) - 97]
            if jmpInd == -1:
                continue

            # s1 and s2 are same
            if it == s[ind]:

                # ignoring score of s[jumpInd]
                temp = preScore[jmpInd] - preScore[ind + 1] + dp[jmpInd]
                score = max(score, temp)

            # s1 and s2 are different
            else:
                temp = preScore[jmpInd] - preScore[ind] + dp[jmpInd]
                score = max(score, temp)

        # maximum score for each index
        dp[ind] = score

    return dp[0]


if __name__ == '__main__':
    s = "forgfg"
    jumps = [['f', 'r'], ['r', 'g']]

    res = maxScore(s, jumps)
    print(res)



