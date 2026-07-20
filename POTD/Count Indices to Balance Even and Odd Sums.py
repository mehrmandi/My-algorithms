# [Expected Approach] Using Prefix and Suffix Sum– O(n) Time and O(1) Space-------------------

def cntWays(arr):
    n = len(arr)
    res = 0

    # calculate initial right side sums
    rightOddSum = 0
    rightEvenSum = 0
    for i in range(n):
        if i % 2 == 0:
            rightEvenSum += arr[i]
        else:
            rightOddSum += arr[i]

    # initialize left side sums
    leftOddSum = 0
    leftEvenSum = 0

    # check for each index
    for i in range(n):

        # remove current element from right side
        if i % 2 == 0:
            rightEvenSum -= arr[i]
        else:
            rightOddSum -= arr[i]
        # after removing element at index i, indices shift
        # So right side odd becomes even and even becomes odd
        if leftOddSum + rightEvenSum == \
                leftEvenSum + rightOddSum:
            res += 1
        
        # add current element to left side
        if i % 2 == 0:
            leftEvenSum += arr[i]
        else:
            leftOddSum += arr[i]
            

    return res


if __name__ == "__main__":
    arr = [3, 6, 5, 10, 11, 9, 6]
    print(cntWays(arr))


