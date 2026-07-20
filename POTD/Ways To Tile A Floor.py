def nthFibonacci(n):
    a = 1
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

def numberOfWays(n):
    return nthFibonacci(n)

n = 4
print(numberOfWays(n))
    