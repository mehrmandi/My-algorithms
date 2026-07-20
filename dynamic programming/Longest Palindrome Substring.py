def check(start, end , s, n):
    while start > 0 and end < n:
        if s[start - 1] == s[end + 1]:
            return check(start - 1, end + 1, s, n)
        else:
            return start, end
    return start, end



def longPalindrome(s):
    n = len(s)
    max_palin = s[0]
    max_len = 1

    for i in range(0, n - 1):
        start, end = check(i, i, s, n - 1)
        if end - start + 1 > max_len:
            max_len = end - start + 1
            max_palin = s[start:end + 1]
        if s[i] == s[i + 1]:
            start, end = check(i, i + 1, s, n - 1)
            if end - start + 1 > max_len:
                max_len = end - start + 1
                max_palin = s[start:end + 1]

    return max_palin


arr = "bbabcbcab"
print(longPalindrome(arr))
