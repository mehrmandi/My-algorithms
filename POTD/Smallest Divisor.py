def minSumDividing(arr, k):
    left, right = 1, max(arr)

    def sum_divided(s):
        # Equivalent to ceil(num / s)
        return sum(-(-num//s) for num in arr)

    while left < right:
        mid = (left + right) // 2
        if sum_divided(mid) <= k:
            print(mid, sum_divided(mid))
            right = mid  # Search for smaller `s`
        else:
            left = mid + 1  # Increase `s`

    return left


arr = [1, 1, 1, 1]
k = 4
print(minSumDividing(arr, k))
