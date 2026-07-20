def bitonic(arr):
    n = len(arr)
    if n == 0:
        return 0
    max_len = 1
    start = 0
    next_start = 0
    j = 0
    while j < n - 1:

        # look for the end of the ascent
        while j < n - 1 and arr[j] <= arr[j + 1]:
            j += 1

        # look for the end of the descent
        while j < n - 1 and arr[j] >= arr[j + 1]:

            # adjusting next_start; this will be
            # executed when we detect the start of the descent
            if j < n - 1 and arr[j] > arr[j + 1]:
                next_start = j + 1
            j += 1

        max_len = max(max_len, j - start+1)
        start = next_start
    return max_len


        

arr = [4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5]
print(bitonic(arr))
