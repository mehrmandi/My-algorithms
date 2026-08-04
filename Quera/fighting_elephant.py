n, m = [int(x) for x in input().split(" ")]

chess = []

max_elephants = []

for i in range(n):
    c = input()
    chess.append(c)

dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]

def heapPermutation(a, size, c, x, y, n, m):

    if size == 1:
        bfs(c, x, y, n, m, a)


    for i in range(size):
        heapPermutation(a, size - 1, c, x, y, n, m)
        if size & 1:
            a[0], a[size - 1] = a[size - 1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]



def markDanger(c, d, x, y):

    dirr = [[1, 1], [-1, 1], [1, -1], [-1, -1]]


    for i in range(4):
        xd = x
        yd = y
        # print("befor", xd, yd)
        while c[xd][yd] == ".":
            xd = xd + dirr[i][0]
            yd = yd + dirr[i][1]
            # print("after", xd, yd)

            if xd < 0 or yd < 0 or xd >= n or yd >= m:
                # print("break")
                break

            elif c[xd][yd] == "#":
                # print("#")
                break
            # print("c[xd][yd]", c[xd][yd])
            # print("danger")
            d[xd][yd] = "red"

    return d



def bfs(c, x, y, n, m, dir):
    global max_elephants
    # print("x, y", x, y)
    # print(dir)

    visited = [["white" for _ in range(m)] for _ in range(n)]
    danger = [["white" for _ in range(m)] for _ in range(n)]

    elephants = []

    if c[x][y] == ".":
        # print(x, y)
        elephants = [[x, y]]


    q = []
    q.append([x, y])
    visited[x][y] = "orange"
    # print("befor", danger)
    markDanger(c, danger, x, y)
    # print("after", danger)


    while len(q)> 0:
        sz = len(q)
        # print("q", q)
        for i in range(sz):
            curr = q.pop(0)
            x1, y1 = curr

            for i in range(4):
                # print("dir", dir)
                newX = x1 + dir[i][0]
                newY = y1 + dir[i][1]
                # print("sus", newX, newY)

                if 0 <=newX < n and 0 <=newY < m:
                    if c[newX][newY] == "." and visited[newX][newY] == "white":
                        if danger[newX][newY] == "white":
                            # print("newX, newY", newX, newY)
                            q.append([newX, newY])
                            elephants.append([newX, newY])
                            visited[newX][newY] = "orange"
                            # print("befor1", danger)
                            danger = markDanger(c, danger, newX, newY)
                            # print("after1", danger)
                        elif danger[newX][newY] == "red":
                            q.append([newX, newY])
                            visited[newX][newY] = "orange"

                    if c[newX][newY] == "#" and visited[newX][newY] == "white":
                        q.append([newX, newY])
                        visited[newX][newY] = "orange"
    print("x,y", x, y)
    # print("ele", el)
    print(len(elephants))
    print("elephants", elephants)

    if len(elephants) > len(max_elephants):
        max_elephants = elephants



for i in range(n):
    for j in range(m):
        heapPermutation(dir, 4, chess, i, j, n, m)



print(len(max_elephants))

for i in max_elephants:
    print(i[0] + 1, i[1] + 1, sep=" ")