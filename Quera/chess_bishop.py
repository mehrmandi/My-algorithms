#  n is the nuumber of rows
#  m is the number of columns
n, m = [int(x) for x in input().split(" ")]



def bishopLocation(n, m):
    for i in range(n):
        for j in range(m):
            if i == 0:
                print("A", end="")
            elif i == n - 1:
                print("B", end="")
            elif j == 0 and (i != 0 or i != n - 1):
                print("A", end="")
            elif j == m - 1 and (i != 0 or i != n - 1):
                print("B", end="")
            else:
                print(".", end="")
        print("")


bishopLocation(n, m)