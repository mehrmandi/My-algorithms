def nextLargerElement(arr):
    # code here
    n = len(arr)
    res = [-1] * n
    max_num = max(arr)
    max_index = arr.index(max_num)
    shift = n - max_index - 1
    
    new_arr = arr[max_index + 1:] + arr[:max_index + 1]
    
    stk = []

    for i in range(n - 1, -1, -1):

        while stk and new_arr[stk[-1]] <= new_arr[i]:
            stk.pop()

        if stk:
            res[i - shift] = new_arr[stk[-1]]
            

        stk.append(i)

    return res


arr = [57, 78, 5, 21, 90, 50, 0, 46, 18, 42, 57, 78, 5, 21, 90, 50, 0, 46, 18, 42]

print(nextLargerElement(arr))


# def nextGreater(arr):
#     n = len(arr)
#     res = [-1] * n
#     stk = []

#     # Traverse the array from right to left
#     for i in range(2 * n - 1, -1, -1):

#         # Pop elements from the stack that are less
#         # than or equal to the current element
#         while stk and stk[-1] <= arr[i % n]:
#             stk.pop()

#         # If the stack is not empty, the top element
#         # is the next greater element
#         if i < n and stk:
#             res[i] = stk[-1]

#         stk.append(arr[i % n])

#     return res


# if __name__ == "__main__":
#     arr = [1, 3, 2, 4]
#     ans = nextGreater(arr)
#     for x in ans:
#         print(x, end=" ")

# arr = [57, 78, 5, 21, 90, 50, 0, 46, 18, 42, 57, 78, 5, 21, 90, 50, 0, 46, 18, 42]
# print(nextGreater(arr))
