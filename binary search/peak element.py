def peakElement(arr):
    n = len(arr)

    # If there is only one element, then it's a peak
    if n == 1:
        return 'true'

    # Check if the first element is a peak
    if arr[0] > arr[1]:
        return 'true'

    # Check if the last element is a peak
    if arr[n - 1] > arr[n - 2]:
        return 'true'

    # Search Space for binary Search
    lo, hi = 1, n - 2

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        print(mid)
        # If the element at mid is a
        # peak element return mid
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            print(arr[mid], arr[mid + 1])

            return 'true'

        # If next neighbor is greater, then peak
        # element will exist in the right subarray
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1

        # Otherwise, it will exist in left subarray
        else:
            hi = mid - 1

    return 'false'


if __name__ == "__main__":
    arr = [1, 2, 4, 5, 7, 8, 3]
    print(peakElement(arr))