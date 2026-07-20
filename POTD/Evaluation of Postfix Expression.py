# def operate(op, a, b):
#     if ord(op) == 43:
#         return a + b
#     if ord(op) == 45:
#         return a - b
#     if ord(op) == 42:
#         return a * b
#     if ord(op) == 47:
#         c = a // b
#         if c < 0:
#             return -(abs(a) // abs(b))
#         else:
#             return c





# def evaluationPostfixExp(arr):
#     n = len(arr)
#     st = []
#     if n == 1:
#         return arr[0]

#     for i in range(n):
#         if st:
#             if st[-1] == "+" or st[-1] == "-" or st[-1] == "*" or st[-1] == "/":
#                 op = st.pop()
#                 b = int(st.pop())
#                 a = int(st.pop())
#                 res = operate(op, a, b)
#                 st.append(res)

#         st.append(arr[i])

#     res = operate(st[-1], int(st[0]), int(st[1]))
#     return res


# # arr = ["100", "200", "+", "2", "/", "5", "*", "7", "+"]
# arr = [-8, 3, "/"]
# print(evaluationPostfixExp(arr))


# [Approach] Using Stack - O(n) Time and O(n) Space--------------------------------------


import math


def evaluatePostfix(arr):
    st = []

    for token in arr:

        # If it's an operand (number), push it onto the stack
        if token[0].isdigit() or (len(token) > 1 and token[0] == '-'):
            st.append(int(token))

        # Otherwise, it must be an operator
        else:
            val1 = st.pop()
            val2 = st.pop()

            if token == '+':
                st.append(val2 + val1)
            elif token == '-':
                st.append(val2 - val1)
            elif token == '*':
                st.append(val2 * val1)
            elif token == '/':
                st.append(val2 // val1)
            elif token == '^':
                st.append(int(math.pow(val2, val1)))
    return st.pop()


if __name__ == '__main__':
    arr = ["2", "3", "1", "*", "+", "9", "-"]
    print(evaluatePostfix(arr))
