def smallest_encrypted_string(s):
    n = len(s)

    if n == 0:
        return ""

    BASE = 911382323
    MOD = 10**9 + 7

    # -------------------------
    # Rolling Hash
    # -------------------------

    prefix = [0] * (n + 1)
    power = [1] * (n + 1)

    for i in range(n):
        x = ord(s[i]) - ord('a') + 1

        prefix[i + 1] = (
            prefix[i] * BASE + x
        ) % MOD

        power[i + 1] = (
            power[i] * BASE
        ) % MOD

    def get_hash(l, r):
        return (
            prefix[r]
            - prefix[l] * power[r - l]
        ) % MOD

    def equal(l1, r1, l2, r2):
        return (
            get_hash(l1, r1)
            == get_hash(l2, r2)
        )

    # -------------------------
    # Greedy
    # -------------------------

    ans = []

    k = 0

    while k < n:

        # اگر prefix فعلی را بتوانیم تکرار کنیم
        if k > 0 and 2 * k <= n:

            if equal(0, k, k, 2 * k):
                ans.append('*')
                k *= 2
                continue

        # در غیر این صورت کاراکتر بعدی
        ans.append(s[k])
        k += 1

    return ''.join(ans)


s = "bbbbbbbbbbbbbbbmbbibb"
print(smallest_encrypted_string(s))
