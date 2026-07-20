# Computes the Möbius function up to 'n'
def computeMobius(n, mu):
    is_prime = [1] * (n + 1)
    mu[0] = 0
    mu[1] = 1

    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i, n + 1, i):
                mu[j] *= -1
                is_prime[j] = 0
            # Not square-free
            for j in range(i * i, n + 1, i * i):
                mu[j] = 0

# Builds frequency array for values in 'arr'


def buildFre(arr, freq):
    for x in arr:
        freq[x] += 1

# For each k, computes how many numbers in arr
# are divisible by k


def computeDivCnt(maxVal, freq, d):
    for k in range(1, maxVal + 1):
        for j in range(k, maxVal + 1, k):
            d[k] += freq[j]

# logic to count coprime pairs using
# Möbius and Inclusion-Exclusion


def cntCoprime(arr):
    maxVal = max(arr)

    # d[i] -> number of elements divisible by 'i'
    # mu[i] -> mobius sign for 'i'
    # fre[i] -> frequency of element 'i'

    freq = [0] * (maxVal + 1)
    d = [0] * (maxVal + 1)
    mu = [1] * (maxVal + 1)

    buildFre(arr, freq)
    computeDivCnt(maxVal, freq, d)
    computeMobius(maxVal, mu)

    result = 0
    for k in range(1, maxVal + 1):
        if mu[k] == 0 or d[k] < 2:
            continue

        # number of pairs that are divisible by k
        pairs = d[k] * (d[k] - 1) // 2
        result += mu[k] * pairs

    return result


if __name__ == "__main__":
    arr = [2, 3, 6, 8, 5, 9, 16, 15, 14, 26]
    print(cntCoprime(arr))

Example
arr = [2, 3, 6, 8, 5, 9, 16, 15, 14, 26]


# print(countCoprimes(arr))  # Output: [2, 2, 2, 3, 3, 5, 7]



# def get_unique_primes(n):
#     primes = set()
#     while n % 2 == 0:
#         primes.add(2)
#         n //= 2
#     p = 3
#     while p * p <= n:
#         while n % p == 0:
#             primes.add(p)
#             n //= p
#         p += 2
#     if n > 1:
#         primes.add(n)
#     return sorted(primes)


# # Example
# # print(get_unique_primes(20))  # Output: [2, 3, 5, 7]

# def countCoprime(arr):
#     just_prime = {}
#     other = []
#     other_dic_ex = {}
#     just_primes_len = 0
#     res = 0
    
#     for num in arr:
#         primes = get_unique_primes(num)
#         if len(primes) == 1:
#             just_prime[primes[0]] = just_prime.get(primes[0], 0) + 1
#             just_primes_len += 1
            
#         else:
#             other.append(primes)
    
#     other_len = len(other)
    
#     for i in range(len(other)):
#         for j in range(len(other[i])):
#             other_dic_ex[other[i][j]] = other_dic_ex.get(other[i][j], 0) + 1
            
#     sets = [set(sub) for sub in other]
#     result = []

#     for i in range(len(sets)):
#         count = 0
#         for j in range(len(sets)):
#             if i != j and sets[i].isdisjoint(sets[j]):
#                 count += 1
#         result.append(count)
        
#     print(just_prime, other, just_primes_len, other_len)
#     print(other_dic_ex)
#     print(result)
    
#     for key, val in just_prime.items():
#         just_primes_len -= val
#         exe_other = other_dic_ex[key] if key in other_dic_ex else 0
#         # print("exe_other", val, just_primes_len, exe_other, res)
#         # print("res now", val * (just_primes_len + (other_len - exe_other)))
#         res += val * (just_primes_len + (other_len - exe_other))
        
#     res += sum(result) // 2
    
#     return res
    
    
# arr = [11, 14, 8, 15, 15, 17, 12, 2, 5, 7]
# print(countCoprime(arr))



