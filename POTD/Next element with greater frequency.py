from collections import Counter


def nextGreaterFreq(arr):
    num_count = dict(Counter(arr))
    n = len(arr)
    res = [-1] * n
    stk = []

    for i in range(n - 1, -1, -1):

        while stk and num_count[arr[stk[-1]]] <= num_count[arr[i]]:
            stk.pop()

        if stk:
            res[i] = arr[stk[-1]]

        stk.append(i)

    return res
    

arr = [5, 1, 5, 6, 6]
print(nextGreaterFreq(arr))


# [Efficient Approach] Frequency Counting and Stack - O(n) Time and O(n) Space

# def findGreater(arr):
#     n = len(arr)
#     freq = {}

#     # Build frequency map
#     for num in arr:
#         freq[num] = freq.get(num, 0) + 1

#     res = [-1] * n
#     s = []

#     for i in range(n):

#         # While current frequency is
#         # greater than frequency at stack top
#         while s and freq[arr[i]] > freq[arr[s[-1]]]:
#             res[s.pop()] = arr[i]
#         s.append(i)

#     return res


# if __name__ == "__main__":
#     arr = [2, 1, 1, 3, 2, 1]
#     result = findGreater(arr)
#     print(' '.join(map(str, result)))


    