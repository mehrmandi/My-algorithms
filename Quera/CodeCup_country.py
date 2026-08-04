#  number of cities in length
m = int(input())

#  number of cities in width
n = int(input())

def borderCity(m, n):
    if m == 1:
        print(n)
    elif n == 1:
        print(m)
    else:
        border_city = 2 * (m + n - 2)
        print(border_city)


borderCity(m, n)