# Given a string s which consists of digits, find the sum of all digits across all non-empty subsequences of s.

# Note: Since the answer can be very large, return it modulo 10 ^ 9 + 7.


# Count Contribution of Each Digit - O(n) Time and O(1) Space

def subsequenceSum(s):
    MOD = 10**9 + 7

    digitSum = sum(int(ch) for ch in s) % MOD

    return (digitSum * pow(2, len(s) - 1, MOD)) % MOD
    
    
s = "485107265874226987"
print(subsequenceSum(s))
