# def firstPartion(arr, left, right, target):
#     pivot = arr[target - 1]
#     i = left
#     j = right
#     print(pivot)
#     while i <= j:
#         print("aval", i, j)
#         while arr[i] >= pivot:
#             print("i", i)
#             i += 1
#         while arr[j] < pivot:
#             print("j", j)
#             j -= 1
#
#         if i <= j:
#             print("swap", arr[i], arr[j])
#             swap(arr, i, j)
#             i += 1
#             j -= 1
#
#     return arr[:k]

def partion(arr, left, right):
    pivot = arr[(left + right) // 2]
    i = left
    j = right

    while i <= j:
        while arr[i] > pivot:
            i += 1
        while arr[j] < pivot:
            j -= 1

        if i <= j:
            swap(arr, i, j)
            i += 1
            j -= 1

    return i


def swap(arr, leftIndex, rightIndex):
    arr[leftIndex], arr[rightIndex] = arr[rightIndex], arr[leftIndex]

def quickSort(arr, left, right):
    if len(arr) > 1:
        index = partion(arr, left, right)
        print(index, left, right)

        if left < index - 1:
            quickSort(arr, left, index - 1)

        if index < right:
            quickSort(arr, index, right)

    return arr


def kLargeElement(arr, k):
    n = len(arr)
    arr = quickSort(arr, 0, n - 1)
    return arr[:k]









arr = [1, 23, 12, 9, 30, 2, 50]
k = 3
print(kLargeElement(arr, k))