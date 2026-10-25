# Given a string s, return the sum of the beauty of all substrings of s. The beauty of a substring is defined as the difference between the maximum and minimum frequencies of the characters present in that substring.

# Expand Substrings and Maintain Frequencies - O(n ^ 2) Time and O(26) Space

def beautySum(s: str) -> int:
    n = len(s)
    ans = 0

    for i in range(n):
        cnt = [0] * 26
        max_f = 0

        for j in range(i, n):
            idx = ord(s[j]) - ord('a')
            cnt[idx] += 1
            max_f = max(max_f, cnt[idx])

            min_f = n + 1
            for freq in cnt:
                if freq > 0:
                    min_f = min(min_f, freq)

            ans += max_f - min_f

    return ans
            
    

s = "aabc"
print(beautySum(s))
