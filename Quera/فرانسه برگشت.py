import sys


def solve():
    input = sys.stdin.buffer.readline

    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))

    pref = [0] * (n + 1)

    s = 0
    for i, x in enumerate(a, 1):
        s = (s + x) % m
        pref[i] = s

    vals = sorted(set(pref))
    rank = {v: i + 1 for i, v in enumerate(vals)}

    size = len(vals)
    NEG = -10**30

    bit_left = [NEG] * (size + 1)
    bit_right = [NEG] * (size + 1)

    def update(bit, i, value):
        while i <= size:
            if value > bit[i]:
                bit[i] = value
            i += i & -i

    def query(bit, i):
        result = NEG
        while i > 0:
            if bit[i] > result:
                result = bit[i]
            i -= i & -i
        return result

    dp = [NEG] * (n + 1)
    dp[0] = 0

    add_ptr = 0

    for i in range(1, n + 1):

        while add_ptr <= i - k:
            r = rank[pref[add_ptr]]
            value = dp[add_ptr] - pref[add_ptr]

            update(bit_left, r, value)

            reverse_r = size - r + 1
            update(bit_right, reverse_r, value)

            add_ptr += 1

        r = rank[pref[i]]

        best = NEG

        x = query(bit_left, r)

        if x != NEG:
            best = x + pref[i]

        reverse_r = size - r
        x = query(bit_right, reverse_r)

        if x != NEG:
            best = max(best, x + pref[i] + m)

        dp[i] = best

    print(dp[n])


if __name__ == "__main__":
    solve()
    
    
        
