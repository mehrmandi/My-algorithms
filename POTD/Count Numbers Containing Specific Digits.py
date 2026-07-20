def countValid(n, arr):
    flag = 0 in arr
    all_num = 9 * (10 ** (n - 1))
    num = len(set(arr))
    not_valid = 0

    if not flag:
        not_valid = (9 - num) * ((10 - num) ** (n - 1))

    else:
        not_valid = (10 - num) * ((10 - num) ** (n - 1))

    return all_num - not_valid
        
    
n = 9
arr = [0, 1, 2, 3, 5]
print(countValid(n, arr))


# Time Complexity: O(log(n))---------------------------------------------------
# Space Complexity: O(1)-------------------------------------------------------


# Fast exponentiation in ints
# def fastpow(base, exp):
#     result = 1
#     while exp > 0:
#         if exp & 1:
#             result *= base
#         base *= base
#         exp >>= 1
#     return result


# def countValid(n, arr):
#     # mark which digits are “good”
#     good = [False] * 10
#     for d in arr:
#         good[d] = True

#     # count forbidden digits overall (f)
#     # and for the first position (f0)
#     f = 0
#     f0 = 0
#     for d in range(10):
#         if not good[d]:
#             f += 1
#             if d != 0:
#                 f0 += 1

#     # total n-digit numbers = 9 * 10^(n-1)
#     total = 9 * fastpow(10, n - 1)

#     # numbers with no good digit = f0 * f^(n-1)
#     none_allowed = f0 if n == 1 else f0 * fastpow(f, n - 1)

#     # valid = total − noneAllowed
#     return total - none_allowed


# if __name__ == "__main__":
#     n = 9
#     arr = [0, 1, 2, 3, 5]
#     print(countValid(n, arr))
