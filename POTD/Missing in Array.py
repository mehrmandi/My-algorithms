def findMissing(arr):
    n = len(arr) + 1
    expected_sum = sum([x for x in range(n + 1)])
    sum_num = sum(arr)
    return expected_sum - sum_num


arr = [1, 2, 3, 4]
print(findMissing(arr))
