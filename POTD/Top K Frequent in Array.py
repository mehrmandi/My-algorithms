# from collections import Counter

# def topKFreq(arr, k):
#     elem_count = Counter(arr)
#     res = []
#     elem_count = [(count, elem) for elem, count in elem_count.items()]
#     sorted_data = sorted(elem_count, key=lambda x: (-x[0], -x[1]))
    
#     for i in range(k):
#         res.append(sorted_data[i][1])
    
#     return res


# arr = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
# k = 4

# print(topKFreq(arr, k))


import random


# Partition function for quickselect


def partition(left, right, pivotIdx, distinct, freq_map):
    pivotFreq = freq_map[distinct[pivotIdx]]
    pivotVal = distinct[pivotIdx]

    distinct[pivotIdx], distinct[right] = distinct[right], distinct[pivotIdx]

    j = left
    for i in range(left, right):

        # Place elements with smaller frequency OR smaller value first
        # So top-k (highest freq, largest value) end up at the end
        if freq_map[distinct[i]] < pivotFreq or (freq_map[distinct[i]] == pivotFreq and distinct[i] < pivotVal):
            distinct[i], distinct[j] = distinct[j], distinct[i]
            j += 1

    distinct[j], distinct[right] = distinct[right], distinct[j]
    return j

# Quickselect function to partially sort the array


def quickselect(left, right, k, distinct, freq_map):
    if left >= right:
        return

    pivotIdx = left + random.randint(0, right - left)
    pivotIdx = partition(left, right, pivotIdx, distinct, freq_map)

    if pivotIdx == k:
        return
    elif pivotIdx > k:
        quickselect(left, pivotIdx - 1, k, distinct, freq_map)
    else:
        quickselect(pivotIdx + 1, right, k, distinct, freq_map)

# Function to find top k frequent elements


def topKFreq(arr, k):
    freq_map = {}
    distinct_set = set()

    # Count frequency of each element
    for val in arr:
        freq_map[val] = freq_map.get(val, 0) + 1
        distinct_set.add(val)

    distinct = list(distinct_set)
    n = len(distinct)

    # Quickselect to move top k frequent elements to the end
    quickselect(0, n - 1, n - k, distinct, freq_map)

    # Sort top k elements by frequency descending, then value descending
    top_k = distinct[n - k:]
    top_k.sort(key=lambda x: (freq_map[x], x), reverse=True)

    return top_k


if __name__ == "__main__":
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    k = 2
    res = topKFreq(arr, k)
    print(" ".join(str(x) for x in res))
