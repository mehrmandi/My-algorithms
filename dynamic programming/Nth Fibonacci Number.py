# def nthFibonacci(n):
#     while n >= 0:
#         if n == 0:
#             return 0
#
#         if n == 1:
#             return 1
#
#         else:
#             return nthFibonacci(n - 2) + nthFibonacci(n - 1)


def nthFibonacci(n):
    a = 0
    b = 1

    if n < 0:
        return False

    elif n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        for n in range(1, n):
            c = a + b
            a = b
            b = c
        return b



print(nthFibonacci(30))