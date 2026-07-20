# from bisect import bisect_left


# class SegmentTree:
#     def __init__(self, size):
#         self.tree = [0] * (2 * size)
#         self.size = size

#     def update(self, index):
#         index += self.size
#         self.tree[index] += 1
#         while index > 1:
#             index //= 2
#             self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

#     def query(self, left, right):
#         left += self.size
#         right += self.size
#         result = 0
#         while left < right:
#             print("left, right", left, right, result)
#             if left % 2:
#                 result += self.tree[left]
#                 left += 1
#             if right % 2:
#                 right -= 1
#                 result += self.tree[right]
#             left //= 2
#             right //= 2
#         return result


# def count_reverse_pairs(arr):
#     sorted_vals = sorted(set(arr + [x // 2 for x in arr]))
#     print(sorted_vals)
#     index_map = {val: idx for idx, val in enumerate(sorted_vals)}
#     tree = SegmentTree(len(sorted_vals))
#     print("tree", tree.tree)
#     count = 0

#     for num in reversed(arr):
#         half_index = bisect_left(sorted_vals, num / 2)
#         print(num, half_index)
#         count += tree.query(0, half_index)
#         tree.update(index_map[num])

#     return count


# # Example
# arr = [3, 2, 4, 5, 1, 20]
# print(count_reverse_pairs(arr))  # Output: 3
# -------------------------------------------------------------------------------------------------------

def merging(arr, low, mid, high):

    count = 0
    j = mid + 1

    # Count valid pairs before merging
    for i in range(low, mid + 1):
        while j <= high and arr[i] > 2 * arr[j]:
            j += 1
        count += (j - (mid + 1))

    # Merge step (standard merge sort)
    temp = []
    left, right = low, mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return count

# Function to perform merge sort and count pairs


def mergeSort(arr, low, high):

    if low >= high:
        return 0

    mid = low + (high - low) // 2
    count = (mergeSort(arr, low, mid) +
             mergeSort(arr, mid + 1, high) +
             merging(arr, low, mid, high))

    return count

# Function to count reverse pairs


def countRevPairs(arr):
    return mergeSort(arr, 0, len(arr) - 1)


if __name__ == "__main__":

    arr = [3, 2, 4, 5, 1, 20]

    print(countRevPairs(arr))


