import random

n, m = [int(x) for x in input().split(" ")]
letters = "acdefghijlmnopqrstuvwxyz"
random_letters = []

for i in range(m):
    random_letter = random.choice(letters)
    random_letters += random_letter

def chocolateArray(row, col, rl):
    graph = [[0 for _ in range(col)] for _ in range(row)]
    columns = [[] for _ in range(col)]
    visited = [[False for _ in range(col)] for _ in range(row)]
    oneness = [[False for _ in range(row)] for _ in range(col)]


    for i in range(row):
        rl = [int(x) for x in input().split(" ")]
        graph[i] = [0 for _ in range(col)]
        for j in range(col):
            columns[j].append(rl[j])
        graph[i] = [0 for _ in range(col)]
        graph[i][0] = rl[0]
        oneness[rl[0] - 1][i] = True
        visited[i][0] = True

    q = []

    for i in range(1, col):
        q.extend(columns[i])
        while q:
            sz = len(q)
            for j in range(sz):
                curr = q.pop(0)
                n = 0
                flag = False
                n = 0
                while n < row:
                    if not oneness[curr - 1][n]:
                        if not visited[n][i]:
                            graph[n][i] = curr
                            visited[n][i] = True
                            oneness[curr - 1][n] = True
                            flag = True
                            break
                    n += 1
                if not flag:
                    n = 0
                    s = 0
                    sub_value = 0
                    while n < row and not flag:
                        if not oneness[curr - 1][n]:
                            sub_value = graph[n][i]
                            while s < row and not flag:
                                if not visited[s][i]:
                                    if not oneness[sub_value - 1][s]:
                                        graph[s][i] = sub_value
                                        graph[n][i] = curr
                                        oneness[curr - 1][n] = True
                                        oneness[sub_value - 1][s] = True
                                        oneness[sub_value - 1][n] = False
                                        visited[s][i] = True
                                        flag = True
                                        break
                                s += 1
                        n += 1

    return graph

for i in chocolateArray(n, m, random_letters):
    for j in i:
        print(j, end=" ")
    print()
