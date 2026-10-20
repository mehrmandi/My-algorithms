# Given an array arr[], you are allowed to perform swap two adjacent arr[i] and arr[i + 1] only if arr[i] + arr[i + 1] is even. Find the lexicographically largest array that can be obtained with this operation applied any number of times(including 0 times).

# Note: An array X is lexicographically larger than another array Y if, at the first position where they differ, X has the larger element.

# Sorting Same-Parity Groups - O(n log n) Time and O(log n) Space

def lexicographicallyLargest(arr: list[int]) -> list[int]:
    n = len(arr)
    i = 0

    # Process each maximal contiguous subarray having the same parity.
    while i < n:
        j = i + 1

        while j < n and arr[j] % 2 == arr[j - 1] % 2:
            j += 1

        # Sort the current subarray in descending order.
        arr[i:j] = sorted(arr[i:j], reverse=True)

        i = j

    return arr


arr = [1, 3, 5]
print(lexicographicallyLargest(arr))
            



