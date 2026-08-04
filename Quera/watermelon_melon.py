#  number of watermelons
h = int(input())

#  number of melons
k = int(input())


def canDivide(watermelon, melon):
    watermelon_rest = watermelon % 2
    melon_rest = melon % 2

    if melon == 0:
        if watermelon_rest == 0:
            print("YES")
        else:
            print("NO")
    else:
        if melon_rest == 0:
            print("YES")
        else:
            print("NO")




canDivide(h, k)