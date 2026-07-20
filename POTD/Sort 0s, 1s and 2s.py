# # Time Complexity: O(2 × n), where n is the number of elements in the array
# # Auxiliary Space: O(1)

# def sort012(arr):
#     n = len(arr)
    
#     count0 = 0
#     count1 = 0
#     count2 = 0
    
#     for i in range(n):
#         if arr[i] == 0:
#             count0 += 1
        
#         elif arr[i] == 1:
#             count1 += 1
            
#         else:
#             count2 += 1
            
#     for i in range(count0):
#         arr[i] = 0
        
#     for i in range(count0, count0 + count1):
#         arr[i] = 1
    
#     for i in range(count0 + count1, n):
#         arr[i] = 2
        
#     return arr
        

# arr = [0, 1, 2, 0, 1, 2]

# print(sort012(arr))


# [Expected Approach] Dutch National Flag Algorithm - One Pass - O(n) Time and O(1) Space----------------
def sort012(arr):
    n = len(arr)

    # initialize three pointers:
    # lo: boundary for 0s
    # mid: current element being checked
    # hi: boundary for 2s
    lo = 0
    hi = n - 1
    mid = 0

    # process elements until mid crosses hi
    while mid <= hi:
        if arr[mid] == 0:

            # current is 0: swap with lo and move both
            # pointers forward
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            # current is 1: it's already in correct position
            mid += 1
        else:
            # current is 2: swap with hi and move hi backward
            # do not increment mid, as swapped value needs
            # to be re-checked
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
            
            

