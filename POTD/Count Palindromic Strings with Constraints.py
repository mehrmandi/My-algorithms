# Given two integers n and k, consider an alphabet consisting of the first k lowercase English letters. Find the number of palindromic strings whose length is less than or equal to n, such that:

# Every character in the string belongs to the given alphabet.
# No character appears more than twice in the string.
# Note: Since the answer can be very large, return it modulo 10 ^ 9+7.

# Time : O(min(n, k))
# space : O(1)

def palindromicStrings(n, k):
    MOD = 10**9 + 7

    res = 0
    ways = 1

    for half in range(1, (n + 1) // 2 + 1):

        if half > k:
            break

        ways = (ways * (k - half + 1)) % MOD

        # length = 2*half - 1
        if 2 * half - 1 <= n:
            res = (res + ways) % MOD

        # length = 2*half
        if 2 * half <= n:
            res = (res + ways) % MOD

    return res

n = 5
k = 8
print(palindromicStrings(n, k))
            
            
            
    
    
