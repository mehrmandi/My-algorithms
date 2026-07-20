def countWays(n):
    a = 1
    b = 2
    c = 4

    if n == 1:
        return 1

    elif n == 2:
        return 2

    elif n == 3:
        return 4

    else:
        for n in range(3, n):
            d = a + b + c
            a = b
            b = c
            c = d
        return c


print(countWays(8))