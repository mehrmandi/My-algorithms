# [Expected Approach] Using Binary Search - O(log n) time and O(1) space------------------


def isGreater(val, d):
    digitSum = 0
    tmp = val
    while tmp > 0:
        digitSum += tmp % 10
        tmp //= 10
    return val - digitSum >= d


def getCount(n, d):

    # Minimum number for which difference between
    # number and sum of digits >= d.
    mini = n + 1
    s = 1
    e = n

    while s <= e:
        mid = s + (e - s) // 2
        if isGreater(mid, d):
            mini = mid
            e = mid - 1
        else:
            s = mid + 1

    # Number of values in range [1, n]
    # will be equal to
    return n + 1 - mini


n = 985476
d = 9999
print(getCount(n, d))


# 859575610
