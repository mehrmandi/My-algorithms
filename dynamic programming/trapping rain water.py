# def nextLargerElement(arr):
#     n = len(arr)
#     res = [-1] * n
#     stk = []
#
#     for i in range(n - 1, -1, -1):
#         while stk and arr[stk[-1]] <= arr[i]:
#             stk.pop()
#
#         if stk:
#             print(i, stk[-1])
#             res[i] = stk[-1]
#             print(res)
#
#         stk.append(i)
#
#     return res


#
# def previousLargerElement(arr):
#     n = len(arr)
#     res = [-1] * n
#     stk = []
#
#     for i in range(n):
#         while stk and arr[stk[-1]] < arr[i]:
#             stk.pop()
#
#         if stk:
#             # print(i, stk)
#             res[i] = stk[-1]
#             # print(res)
#
#         stk.append(i)
#
#     return res
#
#
# def trappedWater(arr):
#     n = len(arr)
#     res = list(zip(previousLargerElement(arr), nextLargerElement(arr)))
#     print(res)
#     max_water = 0
#
#     for i in range(n):
#         tup = res[i]
#         if not (tup[0] == -1 or tup[1] == -1) and res[i] != res[i - 1]:
#             water = (abs(tup[1] - tup[0]) - 1) * (min(arr[tup[0]], arr[tup[1]]) - arr[i])
#             # print(i, water, max_water)
#             max_water += water
#
#     # print(res)
#     return max_water
#
# --------------------------------------------------------------------------------------------

def maxWater(arr):
    st = []
    res = 0

    for i in range(len(arr)):

        # Pop all items smaller than arr[i]
        while st and arr[st[-1]] < arr[i]:
            print("while", i, st)
            pop_height = arr[st.pop()]
            print("pop", pop_height)

            if not st:
                break


            distance = i - st[-1] - 1
            print("dist", distance)

            water = min(arr[st[-1]], arr[i])
            print("water", st, arr[i], water)

            water -= pop_height

            res += distance * water
            print("res", res)
        st.append(i)

    return res

arr = [82, 67, 41, 32, 73, 16, 9, 53, 78, 66, 6, 47, 69, 78, 1, 14, 42, 36, 17, 49, 79]


# print(maxWater(arr))
# print(stockSpan(arr))
# print(nextLargerElement(arr))
# print(previousLargerElement(arr))
print(maxWater(arr))


