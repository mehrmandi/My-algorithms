# def maxWater(arr):
#     n = len(arr)
#     left, right = 0, n - 1
#     res = 0
#     min_val = -1
    
#     while left < right:
#         sm = left if arr[left] <= arr[right] else right
#         res = max(res, (right - left) * arr[sm])
#         min_val = arr[sm]
#         print("sm, res, min_val", sm, res, min_val)
        
#         if sm == left:
#             left += 1
#             while arr[left] <= min_val and left < right:
#                 left += 1
#         print("left", left)
#         if sm == right:
#             right -= 1
#             while arr[right] <= min_val and left < right:
#                 right -= 1
#         print("right", right)
#     return res


# arr = [9, 6, 2, 9, 2, 9, 5, 5]
# print(maxWater(arr))

# 2 5 10 4 2 1 6 6 5 5 9 1 2 4 7
# 84



# [Expected Approach] Using Two Pointers - O(n) Time and O(1) Space------------------------------------------
def maxWater(arr):
    left = 0
    right = len(arr) - 1
    res = 0
    while left < right:

        # find the water stored in the container between
        # arr[left] and arr[right]
        water = min(arr[left], arr[right]) * (right - left)
        res = max(res, water)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return res


if __name__ == "__main__":
	arr = [2, 1, 8, 6, 4, 6, 5, 5]
	print(maxWater(arr))




