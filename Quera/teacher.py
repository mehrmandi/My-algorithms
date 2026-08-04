import random
import heapq
import copy

n, m = [int(x) for x in input().split(" ")]
letters = "acdefghijlmnopqrstuvwxyz"
random_letters = []

for i in range(m):
    random_letter = random.choice(letters)
    random_letters += random_letter

def colExchange(row, col, g, rs):
    if g[row][col] not in rs:
        return g[row][col], row
    else:
        if row < len(g) - 1:
            colExchange(row + 1, col, g, rs)
        else:
            return False

def rowArrange(row, col, g):
    for i in range(col):
        if i == 0:
            res = g[row][1:]
        else:
            res = g[row][:i]

        if g[row][i] in res:
            if colExchange(row + 1, i, g, res):
                value, new_row = colExchange(row + 1, i, g, res)
                g[new_row][i] = g[row][i]
                g[row][i] = value
    return g

def chocolateArray(row, col, rl):
    graph = []
    for i in range(row):
        rl = [int(x) for x in input().split(" ")]
        graph.append(rl)
    for i in range(row):
        while len(graph[i]) != len(set(heapq.nlargest(len(graph[i]), graph[i]))):
            rowArrange(i, col, graph)

    return graph



for i in chocolateArray(n, m, random_letters):
    for j in i:
        print(j, end=" ")
    print()


