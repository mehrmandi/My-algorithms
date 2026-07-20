def uniqueNum(arr):
    expected_sum = sum(set(arr)) * 2
    sum_num = sum(arr)
    return expected_sum - sum_num


arr = [1, 2, 1, 5, 5]
print(uniqueNum(arr))
