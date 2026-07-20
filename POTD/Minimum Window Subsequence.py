def minWindowSubsequence(s1: str, s2: str) -> str:
    n, m = len(s1), len(s2)
    min_len = float("inf")
    start_idx = -1

    i = 0
    while i < n:
        j = 0

        # Forward scan to match s2
        while i < n:
            if s1[i] == s2[j]:
                j += 1
                if j == m:
                    break
            i += 1

        if j < m:
            break  # no more subsequences possible

        # Backward scan to minimize window
        end = i
        j = m - 1
        while i >= 0:
            if s1[i] == s2[j]:
                j -= 1
                if j < 0:
                    break
            i -= 1

        i += 1  # move to valid start

        if end - i + 1 < min_len:
            min_len = end - i + 1
            start_idx = i

        i = i + 1  # continue searching

    return "" if start_idx == -1 else s1[start_idx - 1:start_idx + min_len]

                    

# s1 = "geeksforgeeks"
s1 = "geeksforgeeks"
s2 = "eksrg"
print(minWindowSubsequence(s1, s2))

