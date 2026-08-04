x, y = [int(i) for i in input().split(" ")]

def cafenetCap(c, g):
    comp = "0" * c
    for i in range(g):
        flag = True
        s, n = [int(r) for r in input().split(" ")]
        while flag and s + n <= len(comp) + 1:
            if comp[s - 1: s + n - 1] == "0" * n:
                comp = comp[0:s - 1] + "1" * n + comp[s - 1 + n:]
                flag = False
            else:
                s += 1
        print(comp)

cafenetCap(x, y)