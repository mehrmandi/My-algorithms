import sys


def solve():
    a, b = map(int, input().split())
    MOD = 10**9 + 7

    if b <= a:
        print(1)
        return
    
    size = (b // 2) + 1
    is_prime = bytearray(b"\x01") * size
    is_prime[0] = 0  

    limit = int(b**0.5)
    for i in range(1, (limit // 2) + 1):
        if is_prime[i]:
            p = 2 * i + 1
            start = (p * p) // 2
            count = ((size - 1 - start) // p) + 1
            is_prime[start::p] = b"\x00" * count

    primes = [2]
    pi = [0] * (b + 1)
    pi[2] = 1

    for x in range(3, b + 1):
        if x % 2 == 1 and is_prime[x // 2]:
            pi[x] = pi[x - 1] + 1
            if x <= limit:
                primes.append(x)
        else:
            pi[x] = pi[x - 1]

    ans = 1

    for p in primes:
        exponent = 0
        power = p
        while power <= b:
            exponent += (b // power) - (a // power)
            if power > b // p:
                break
            power *= p

        if exponent > 0:
            ans = (ans * (exponent + 1)) % MOD

    low_bound = max(limit + 1, a + 1)

    for x in range(limit + 1, min(b + 1, a + 1)):
        if x % 2 == 1 and is_prime[x // 2]:
            exp = (b // x) - (a // x)
            if exp > 0:
                ans = (ans * (exp + 1)) % MOD

    curr = low_bound
    while curr <= b:
        k = b // curr
        next_val = b // k  

        cnt = pi[min(next_val, b)] - pi[curr - 1]
        if cnt > 0:
            ans = (ans * pow(k + 1, cnt, MOD)) % MOD

        curr = next_val + 1

    print(ans)


if __name__ == "__main__":
    solve()
        
    
    
    
    