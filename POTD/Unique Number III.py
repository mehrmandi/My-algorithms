def uniqueNumber(arr):
    expected_sum = sum(set(arr)) * 3
    sum_num = sum(arr)
    return (expected_sum - sum_num) // 2



arr = [3, 2, 1, 34, 34, 1, 2, 34, 2, 1]
print(uniqueNumber(arr))