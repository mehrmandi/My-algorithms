# [Naive Approach] Factorial Division Method O(n) Time and O(1) Space---------------------------------------
# 
# 
# def kDividing(x, k, res):
#     if x < k:
#         return res

#     if x % k == 0:
#         res[0] += 1
#         kDividing(x // k, k, res)

#     return res


# def factorial(n):
#         if n == 0 or n == 1:
#             return 1
#         return n * factorial(n - 1)


# def maxKPower(n, k):
#     res = [0]
#     n_fac = factorial(n)
        
#     return kDividing(n_fac, k, res)[0]




# [Expected Approach] Legendre’s Method for Composite Divisibility--------------------------------------------------

# Time Complexity: O(√k + m * log n), where m is number of distinct prime factors in k, O(√k) for prime factorization of k and log n for apply Legendre formula for each prime factor of k.
# Auxiliary Space: O(m), where m is number of distinct prime factors in



from collections import Counter
import math


def prime_factors(k):
    """Return the prime factorization of k as a dictionary {prime: exponent}"""
    factors = Counter()
    i = 2
    while i * i <= k:
        while k % i == 0:
            factors[i] += 1
            k //= i
        i += 1
    if k > 1:
        factors[k] += 1
    return factors


def count_factor_in_factorial(n, p):
    """Count how many times prime p appears in n! using Legendre's formula"""
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count


def max_power_dividing_factorial(n, k):
    """Compute the maximum x such that k^x divides n!"""
    factors = prime_factors(k)
    print("factors", factors)
    min_x = float('inf')
    for prime, exponent in factors.items():
        count_in_fact = count_factor_in_factorial(n, prime)
        x = count_in_fact // exponent
        min_x = min(min_x, x)
    return min_x


# Time Complexity: O(√k + m × n log n), O(√k) for factorization and O(m × n log n) for counting divisions, where m is the number of prime factors of k (m is nearly equal to log k).
# Auxiliary Space: O(log k) for unique prime factors the factors of k.---------------------------------------------------------------------------------------
# def primeFactors(num):
#     # Function to compute the prime
#     # factorization of a number 'num'
#     factors = []

#     # Count the number of times 2 divides 'num'
#     count = 0
#     while num % 2 == 0:
#         num //= 2
#         count += 1
#     if count > 0:
#         factors.append([2, count])

#     # Check for odd factors starting from 3
#     i = 3
#     while i * i <= num:
#         count = 0
#         while num % i == 0:
#             num //= i
#             count += 1
#         if count > 0:
#             factors.append([i, count])
#         i += 2

#     # If 'num' is still greater than 1, it's a prime number
#     if num > 1:
#         factors.append([num, 1])

#     return factors


# def maxKPower(n, k):
#     # Step 1: Get the prime factorization of k
#     factors = primeFactors(k)

#     # Initialize result to maximum possible, we'll
#     # take the minimum across all primes
#     result = float('inf')

#     # For each prime factor of k
#     for prime, freq_in_k in factors:
#         count = 0

#         # Count how many times 'prime' appears
#         # in the factorization of n!
#         for i in range(1, n + 1):
#             x = i
#             # Count how many times 'prime' divides
#             # this particular number
#             while x % prime == 0:
#                 count += 1
#                 x //= prime

#         # Since k = prime^freq_in_k × ...,
#         # we divide the total count by freq_in_k
#         result = min(result, count // freq_in_k)

#     return result


# if __name__ == "__main__":
#     n = 10
#     k = 9
#     print(maxKPower(n, k))


    
		
	
		
