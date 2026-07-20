# def nonLisMaxSum(arr):
#     n = len(arr)
#     counter = [[1, 0] for i in range(n)]
#     sum_arr = sum(arr)

#     for i in range(1, n):
#         for j in range(i):
#             if arr[j] < arr[i]:
#                 if counter[j][0] + 1 > counter[i][0]:    
#                     counter[i][0] = counter[j][0] + 1
#                     counter[i][1] = counter[j][1] + arr[i]
                    
#                 elif counter[j][0] + 1 == counter[i][0]:
#                     counter[i][0] = counter[j][0] + 1
#                     counter[i][1] = min(counter[j][1] + arr[i], counter[i][1])
                    
#     max_first = max(sub[0] for sub in counter)
#     filtered = [sub for sub in counter if sub[0] == max_first]
#     result = min(filtered, key=lambda x: x[1])

    
#     return sum_arr - result[1]


# arr = [4, 6, 1, 2, 4, 6]

# print(nonLisMaxSum(arr))


from bisect import bisect_right
from collections import OrderedDict

mp = {}

# insert a value into the map while
# maintaining optimal LIS information


def insert(val):
    keys = sorted(mp.keys())
    idx = bisect_right(keys, val)

    length = 1
    total = val

    if idx > 0:
        prev = keys[idx - 1]
        length = mp[prev][0] + 1
        total = mp[prev][1] + val

    toerase = []
    while idx < len(keys):
        k = keys[idx]
        if mp[k][0] > length:
            break
        toerase.append(k)
        idx += 1

    for key in toerase:
        del mp[key]

    mp[val] = [length, total]

# function to compute maximum sum of elements not in the LIS


def nonLisMaxSum(arr):
    mp.clear()
    for val in arr:
        insert(val)
    lisSum = mp[max(mp.keys())][1]
    return sum(arr) - lisSum


def main():
    arr = [4, 6, 1, 2, 3, 8]
    print(nonLisMaxSum(arr))


main()


