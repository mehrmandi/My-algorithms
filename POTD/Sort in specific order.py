
# def sortIt(arr):
#     n = len(arr)
#     i, j = 0, n - 1
    
#     while i <= j:
#         while arr[i] % 2 == 1 and i < j:
#             i += 1
            
#         while arr[j] % 2 == 0 and i <= j:
#             j -= 1
            
#         if i <= j:
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#             j -= 1
    
#     arr[:i] = sorted(arr[:i], reverse=True)
#     arr[i:] = sorted(arr[i:])
            
#     return arr
    

# arr = [19, 5, 21, 1, 19]
# print(sortIt(arr))

# [Expected Approach - 3] Using Custom Comparator - O(n*log(n)) Time and O(1) Space--------------

from functools import cmp_to_key

# Custom compare function


def compare(a, b):

    # When both are even: sort in ascending order
    if a % 2 == 0 and b % 2 == 0:
        return a - b

    # When both are odd: sort in descending order
    if a % 2 == 1 and b % 2 == 1:
        return b - a

    # If one is odd and one is even: odd comes first
    return -1 if a % 2 == 1 else 1

# Function to sort array as per the condition


def sortIt(arr):

    # Sort using the custom comparator
    arr.sort(key=cmp_to_key(compare))


if __name__ == "__main__":

    arr = [1, 2, 3, 5, 4, 7, 10]

    sortIt(arr)

    for x in arr:
        print(x, end=" ")
    