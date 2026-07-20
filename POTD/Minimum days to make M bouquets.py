# def is_potential_day(arr, mid, k, m):
#     i = 0
#     while i < len(arr):
#         j = 0
#         while j < k:
#             if arr[i + j] <= mid:
#                 j += 1
#             else:
#                 i += j + 1
#                 break
#         if j == k:
#             m -= 1
#             i += j
        
#         if m == 0:
#             return True
#     return False
            
    
        
    

# def minDaysBloom(arr, k, m):
#     n = len(arr)
#     if m * k > n:
#         return -1
#     print(arr)
#     sorted_arr = sorted(arr)
#     print(sorted_arr)
    
#     low , high = (m * k) - 1, n - 1
    
#     while low < high:
        
#         mid = (low + high) // 2
        
#         if is_potential_day(arr, sorted_arr[mid], k, m):
#             high = mid
        
#         else:
#             low = mid + 1
            
            
#     return sorted_arr[low]
    
    
        
    
    
    

# m = 3
# k = 2
# arr = [5, 8, 14, 2, 5, 6, 9, 15, 2, 5, 7, 2, 1, 8, 7, 20]
# print(minDaysBloom(arr, k, m))

# Time complexity: O(n × log(maxDays)), where n is the number of elements in the array, and maxDays is the maximum possible number of days for a flower to bloom.
# Auxiliary Space: O(1)
def check(arr, k, m, days):
    bouquets = 0
    cnt = 0

    # iterate through the bloom
    # days of the flowers
    for flower in arr:
        if flower <= days:
            cnt += 1
        else:

            # if the current bloom day count
            # is greater than days, update
            # the bouquets and reset count
            bouquets += cnt // k
            cnt = 0

    bouquets += cnt // k

    # check if current bouquets are greater
    # than or equal to the desired
    # number of bouquets (m)
    return bouquets >= m


def minDaysBloom(arr, k, m):
    lo = 0
    hi = max(arr)
    res = -1

    while lo <= hi:
        mid = (lo + hi) // 2

        if check(arr, k, m, mid):

            # if the current mid is valid update the result
            # and adjust the search range
            res = mid
            hi = mid - 1
        else:

            # if the current mid is not valid
            # adjust the search range
            lo = mid + 1
    return res


if __name__ == "__main__":
    arr = [5, 5, 5, 5, 10, 5, 5]
    k = 3
    m = 2
    print(minDaysBloom(arr, k, m))



