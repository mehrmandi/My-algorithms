# import math


# def simple_sieve(limit):
#     is_prime = [True] * (limit + 1)
#     is_prime[0:2] = [False, False]
#     for i in range(2, int(limit**0.5) + 1):
#         if is_prime[i]:
#             for j in range(i*i, limit + 1, i):
#                 is_prime[j] = False
#     return [i for i, p in enumerate(is_prime) if p]


# def segmented_sieve(n):
#     limit = int(math.sqrt(n)) + 1
#     primes = simple_sieve(limit)
#     result = primes.copy()

#     low = limit
#     high = 2 * limit

#     while low < n:
#         if high > n:
#             high = n
#         is_prime = [True] * (high - low)

#         for p in primes:
#             start = max(p * p, ((low + p - 1) // p) * p)
#             for j in range(start, high, p):
#                 is_prime[j - low] = False

#         for i in range(low, high):
#             if is_prime[i - low]:
#                 result.append(i)

#         low += limit
#         high += limit

#     return result



# def nineDivisors(n):
#     high_range_1 = math.floor(n ** (1/8))
#     print(high_range_1)
#     primes_1 = list(set(segmented_sieve(high_range_1 + 1))) if high_range_1 >= 2 else []
#     print(primes_1)
#     res = len(primes_1)
    
    
#     high_range_2 = math.floor(math.sqrt(n))
#     primes_2 = list(set(segmented_sieve(high_range_2 + 1))) if high_range_2 >= 2 else []
#     primes_2.sort()
#     print(primes_1)
    
#     for i, p in enumerate(primes_2):
#         for j in range(i+1,len(primes_2)):
#             if p * primes_2[j] <= high_range_2:
#                 res += 1
#             else:
#                 break
    
#     return res
    

# n = 5791339

# print(nineDivisors(n))
# # print(segmented_sieve(3))


import math


def countNumbers(n):
    c = 0
    limit = int(math.sqrt(n))

    prime = [i for i in range(limit + 1)]

    # Sieve to store smallest prime factor
    for i in range(2, int(math.sqrt(limit)) + 1):
        if prime[i] == i:
            for j in range(i * i, limit + 1, i):
                if prime[j] == j:
                    prime[j] = i

    for i in range(2, limit + 1):
        p = prime[i]
        q = prime[i // prime[i]]

        # Check for p^2 * q^2 form
        if p * q == i and q != 1 and p != q:
            c += 1
        # Check for p^8 form
        elif prime[i] == i and pow(i, 8) <= n:
            c += 1

    return c


# n = 5791339
# print(countNumbers(n))

