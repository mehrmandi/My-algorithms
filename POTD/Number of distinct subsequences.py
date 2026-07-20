# [Space Optimized] - O(n) Time and O(1) Space------------------

def distinctSubseq(str):
    mod = 10**9 + 7

    dp = 1  # empty subsequence
    last = [0] * 26  # last occurrence contribution

    for ch in str:
        idx = ord(ch) - ord('a')
        new_dp = (dp * 2) % mod
        print("dp", new_dp, last[idx])
        # subtract duplicates caused by previous occurrence
        new_dp = (new_dp - last[idx] + mod) % mod
        
        print("last", last, ch, new_dp)
        

        last[idx] = dp
        dp = new_dp

    return (dp - 1) % mod  # subtract the empty subsequence


str = "ggfggf"
print(distinctSubseq(str))

