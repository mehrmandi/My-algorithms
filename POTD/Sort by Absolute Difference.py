# from functools import cmp_to_key


# def rearrange(arr, x):
#     def myCompare(a, b):
#         if abs(a - x) < abs(b - x):
#             return -1
#         else:
#             return 1
        
        
#     arr.sort(key=cmp_to_key(myCompare))
    
#     return arr    





# x = 7
# arr = [10, 5, 3, 9, 2]
# print(rearrange(arr, x))

# [Approach 2] Using Inbuilt Functions - O(n × logn) Time and O(1) Space
def rearrange(self, arr, x):
    # code here
    n = len(arr)
    # sorting the array using comparator
    arr.sort(key=lambda a: abs(a - x))
