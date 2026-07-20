def missingAP(arr):
    sumVal = sum(arr)
    n = len(arr)
    progStep = float('inf')
    expectedSum = 0

    for i in range(1, 3 if n >= 3 else n):
        dif = arr[i] - arr[i - 1]
        if dif > 0:
            progStep = min(dif, progStep)
            expectedSum = (arr[0] * (n + 1)) + \
                ((((1 + n) * n) // 2) * progStep)

        else:
            dif = -dif
            progStep = min(dif, progStep)
            expectedSum = (arr[0] * (n + 1)) - \
                ((((1 + n) * n) // 2) * progStep)

    return expectedSum - sumVal


arr = [14, 12, 10]
print(missingAP(arr))


# another approach

def findMissing(self, arr):
    n = len(arr)

    diff1 = arr[1] - arr[0]
    diff2 = arr[-1] - arr[-2]
    diff3 = (arr[-1] - arr[0]) // n

       if diff1 == diff2:
            diff = diff1
        elif diff1 == diff3:
            diff = diff1
        else:
            diff = diff2

        if diff == 0:
            return arr[0]

        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            # if mid == (nth position of element in AP)-1
            # the missing element will exist in right half
            if (arr[mid] - arr[0]) // diff == mid:
                lo = mid + 1

            # the missing element will exist in left half
            else:
                hi = mid - 1

        # after breaking out of binary search loop the missing element
        # will exist between high and low
        return arr[hi] + diff
