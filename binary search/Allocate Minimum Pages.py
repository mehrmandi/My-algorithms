def check(arr, k, pageLimit):
    cnt = 1
    pageSum = 0
    for pages in arr:
        if pageSum + pages > pageLimit:
            cnt += 1
            pageSum = pages
        else:
            pageSum += pages


    return cnt <= k


def allocate_page(arr, k):
    if k > len(arr):
        return -1

    low = max(arr)
    high = sum(arr)
    res = -1

    while low <= high:
        mid = low + (high - low) // 2

        if check(arr, k, mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res

arr = [12, 34, 67, 90, 110]
k = 3
print(allocate_page(arr, k))