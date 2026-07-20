# import heapq
# time complexity o(n*2)-----------------------------------------------
# def pairSumCloseZero(arr, n):
#     arr = list(arr)
#     min_heap = []
    
#     for i in range(n):
#         for j in range(i + 1, n):
#             pair_sum = arr[i] + arr[j]
#             print(arr, i, j, pair_sum)
#             tag = 1
#             if pair_sum < 0:
#                 tag = -1
            
#             heapq.heappush(min_heap,(abs(pair_sum), tag))
#             print(min_heap)
            
#     min_value, tag = heapq.heappop(min_heap)
    
#     while min_heap:
#         new_val, new_tag = heapq.heappop(min_heap)
        
#         if new_val > min_value:
#             break
        
#         if new_tag > tag :
#             tag = new_tag
#             break
    
    
#     return min_value * tag

# time complexity o(n*2)-----------------------------------------------
# def pairSumCloseZero(arr, n):
#     arr = list(arr)
#     sudo_zero = False
#     if 0 not in arr:
#         arr.append(0)
#         sudo_zero = True
#     arr.sort()
#     zero_idx = arr.index(0)
#     neg_arr = arr[:zero_idx]
#     n = len(neg_arr)
#     pos_arr = arr[zero_idx:] if not sudo_zero else arr[zero_idx + 1:]
#     m = len(pos_arr)
    
#     neg_sum = neg_arr[n - 1] + neg_arr[n - 2] if n >= 2 else float('-inf')
#     pos_sum = pos_arr[0] + pos_arr[1] if m >= 2 else float('inf')
    
#     for i in range(m):
#         for j in range(n):
#             sum_pair = pos_arr[i] + neg_arr[j]
#             if sum_pair < 0:
#                 neg_sum = max(neg_sum, sum_pair)
#             else:
#                 pos_sum = min(pos_sum, sum_pair)
    
    
#     if abs(pos_sum) <= abs(neg_sum):
#         return pos_sum
#     else:
#         return neg_sum
        
# N = 6
# arr = {-21, -67, -37, -18, 4, -65}
# print(pairSumCloseZero(arr, N))


# time complexity o(nlogn)------------------------------------------------------------

def max_sum_closest_to_zero(arr):
    arr.sort()  # Step 1: Sort the array (O(n log n))
    left, right = 0, len(arr) - 1
    closest_sum = float('-inf')  # Initialize with smallest possible sum

    while left < right:
        curr_sum = arr[left] + arr[right]

        # Update closest sum if necessary
        if abs(curr_sum) < abs(closest_sum) or (abs(curr_sum) == abs(closest_sum) and curr_sum > closest_sum):
            closest_sum = curr_sum

        # Move pointers to try and get closer to zero
        if curr_sum < 0:
            left += 1
        else:
            right -= 1

    return closest_sum


# Example usage
arr = [-8, -66, -60]
print(max_sum_closest_to_zero(arr))  # Output: (-8, -60)

# Time Complexity: O(N2), As we are running a loop of size N2.------------------------------------------
# Space Complexity: O(1), As we are using constant extra space.----------------------------------------
# class Solution:
#     def closestToZero(self, arr, n):
#         # your code here
#         min_l = 0
#         min_r = 1
#         min_sum = arr[0] + arr[1]
#         for l in range(0, n - 1):
#             for r in range(l + 1, n):
#                 sum = arr[l] + arr[r]
#                 if abs(min_sum) > abs(sum):
#                     min_sum = sum
#                     min_l = l
#                     min_r = r
#         return arr[min_l] + arr[min_r]
