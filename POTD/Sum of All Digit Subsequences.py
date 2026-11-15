# Given a string s which consists of digits, find the sum of all digits across all non-empty subsequences of s.

# Note: Since the answer can be very large, return it modulo 10 ^ 9 + 7.


# Count Contribution of Each Digit - O(n) Time and O(1) Space

def subsequenceSum(s):
    MOD = 1000000007
    n = len(s)
    res = 0
    
    for i in range(n):
        res += int(s[i])
        
    return (res * (2 ** (n - 1))) % MOD 
    
    
s = "485107265874226987"
print(subsequenceSum(s))
