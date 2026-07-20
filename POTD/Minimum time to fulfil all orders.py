import math

def donutsByChef(t, r):
    D = 1.0 + 8.0 * t / r
    return int((-1.0 + math.sqrt(D)) / 2.0)

# Checks if all chefs can make at
# least n donuts in time t


def canMake(rank, n, t):
    total = 0
    for r in rank:
        total += donutsByChef(t, r)
        if total >= n:
            return True
    return False

def minTime(rank, n):
    rmin = min(rank)
    hi = rmin * n * (n + 1) // 2
    lo = 0
    ans = hi

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if canMake(rank, n, mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    return ans
    


n = 10
rank = [1, 2, 3, 4]
print(minTime(rank, n))
