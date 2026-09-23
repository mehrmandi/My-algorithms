import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
inp = os.path.join(BASE_DIR, "input.txt")
if os.path.exists(inp):
    sys.stdin = open(inp, "r")


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    a = [int(x) for x in input_data[3: 3 + n]]

    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = (pref[i - 1] + a[i - 1]) % m

    unique_vals = sorted(set(pref))
    val_to_rank = {val: idx for idx, val in enumerate(unique_vals)}
    ranks = [val_to_rank[v] for v in pref]

    num_unique = len(unique_vals)

    size = 1
    while size < num_unique:
        size <<= 1

    NEG_INF = -10**18
    tree = [NEG_INF] * (2 * size)

    def update(pos, val):
        idx = size + pos
        if tree[idx] < val:
            tree[idx] = val
            idx >>= 1
            while idx > 0:
                left_child = tree[2 * idx]
                right_child = tree[2 * idx + 1]
                tree[idx] = (
                    left_child if left_child > right_child else right_child
                )
                idx >>= 1

    def query(l, r):
        if l > r:
            return NEG_INF
        res = NEG_INF
        l += size
        r += size + 1
        while l < r:
            if l & 1:
                if tree[l] > res:
                    res = tree[l]
                l += 1
            if r & 1:
                r -= 1
                if tree[r] > res:
                    res = tree[r]
            l >>= 1
            r >>= 1
        return res

    dp = [NEG_INF] * (n + 1)
    add_ptr = 1

    for i in range(1, n + 1):
        dp[i] = pref[i]

        while add_ptr <= i - k:
            if dp[add_ptr] != NEG_INF:
                update(ranks[add_ptr], dp[add_ptr] - pref[add_ptr])
            add_ptr += 1

        curr_rank = ranks[i]
        curr_val = pref[i]


        left_max = query(0, curr_rank)
        if left_max != NEG_INF:
            cand1 = left_max + curr_val
            if cand1 > dp[i]:
                dp[i] = cand1

        right_max = query(curr_rank + 1, num_unique - 1)
        if right_max != NEG_INF:
            cand2 = right_max + curr_val + m
            if cand2 > dp[i]:
                dp[i] = cand2

    print(dp[n])


if __name__ == "__main__":
    solve()
    
    
        
