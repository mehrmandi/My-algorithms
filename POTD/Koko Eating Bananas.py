def minEatingSpeed(arr, k):
    left, right = 1, max(arr)

    def hours_needed(s):
        # Equivalent to ceil(pile / s)
        return sum(-(-pile // s) for pile in arr)

    while left < right:
        mid = (left + right) // 2
        if hours_needed(mid) <= k:
            right = mid  # Search for smaller `s`
        else:
            left = mid + 1  # Increase `s`

    return left


# Example usage:
arr = [30, 11, 23, 4, 20]
k = 7
print(minEatingSpeed(arr, k))  # Output: Minimum s

