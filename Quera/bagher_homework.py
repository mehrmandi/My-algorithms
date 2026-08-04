a, b, c = [int(x) for x in input().split(" ")]

def isTriangle(a, b, c):
    if a + b + c != 180 or a <= 0 or b <= 0 or c <= 0:
        print("No")
    else:
        print("Yes")


isTriangle(a, b, c)
