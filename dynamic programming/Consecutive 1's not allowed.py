def countStrings(n):
    # code here
    a = 2
    b = 3

    if n < 0:
        return False

    elif n == 1:
        return 2

    elif n == 2:
        return 3

    else:
        for n in range(2, n):
            c = a + b
            a = b
            b = c
        return b


