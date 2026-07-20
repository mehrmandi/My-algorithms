# def wayReachNthStair(n):
#     while n >= 1:
#         if n == 1:
#             return 1
#
#         if n == 2:
#             return 2
#
#         else:
#             return wayReachNthStair(n - 2) + wayReachNthStair(n - 1)

def countWays(n):
    a = 1
    b = 2

    if n == 1:
        return 1

    elif n == 2:
        return 2

    else:
        for n in range(2, n):
            c = a + b
            a = b
            b = c
        return b


print(countWays(6))