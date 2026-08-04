from collections import defaultdict

n, m = [int(x) for x in input().split(" ")]

chess = []

for i in range(n):
    c = input()
    chess.append(c)


def markDanger(c, d, x, y):
    dirr = [[1, 1], [-1, 1], [1, -1], [-1, -1]]


    sq = 0


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
            sq += 1
            d[xd][yd] = "red"

    return d, sq

def calcCost(c, cv, x, y):
    dirr = [[1, 1], [-1, 1], [1, -1], [-1, -1]]

    v = 0

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
            value = cv.get((xd, yd))
            v += value

    return v



def maxBishop(c, n, m):
    danger = [["white" for _ in range(m)] for _ in range(n)]

    chess_value = {}

    bishops = []

    bod = 0

    for i in range(n):
        for j in range(m):
            if c[i][j] == ".":
                bod += 1
                d, sq = markDanger(c, danger, i, j)
                chess_value[(i, j)] = sq

    costs = [[] for _ in range(n * m)]
    max_costs = {}
    # print(bod)

    for i in range(n):
        for j in range(m):
            if c[i][j] == ".":
                bod += 1
                v = calcCost(c, chess_value, i, j)
                max_costs[(i, j)] = v

    # print(max_costs)

    # sorted_value = sorted(chess_value.items(), key=lambda x: x[1])
    # sorted_cost = sorted(max_costs.items(), key = lambda x: x[1], reverse=True)
    nested_dic = defaultdict(dict)

    for key, value in chess_value.items():
        for ckey, cvalue in max_costs.items():
            if key == ckey:
                # print("key, value, ckey, cvalue", key, value, ckey, cvalue)
                nested_dic[key]["remove"] = cvalue
                nested_dic[key]["cost"] = value

    sorted_nested = sorted(nested_dic.items(), key=lambda x: (x[1]["cost"], -x[1]["remove"]))


    danger = [["white" for _ in range(m)] for _ in range(n)]
    # print(chess_value[(1, 2)])
    # print("sorted_value", chess_value)
    # print("sorted_cost", max_costs)
    # print("nested", dict(nested_dic))
    # print(sorted_nested)


    for item in sorted_nested:
        x, y = list(item[0])
        if danger[x][y] == "white":
            danger[x][y] = "red"
            bishops.append([x, y])
            danger, sq = markDanger(c, danger, x, y)

    print(len(bishops))
    print(bishops)






    # for key, value in chess_value.items():
    #     # print(key)
    #     x = key[0]
    #     y = key[1]
    #     costs[value].append([x, y])

    # print(costs)

    #
    # print(len(bishops))
    # print(bishops)










maxBishop(chess, n, m)
