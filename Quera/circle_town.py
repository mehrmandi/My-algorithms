n, m = [int(x) for x in input().split(" ")]

d = [int(x) for x in input().split(" ")]

c = [int(x) for x in input().split(" ")]

def isAccess(d):
    if 0 in d and 1 in d:
        print("YES")
    else:
        print("NO")


isAccess(d)
