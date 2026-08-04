city_graph = [[],
              [2, 3, 4],
              [1, 3, 4, 6, 5],
              [1, 2, 4, 6, 7],
              [1, 2, 3, 5, 6, 7],
              [2, 4, 6],
              [2, 3, 4, 5, 7],
              [3, 4, 6]]


c = int(input())
r = int(input())




def arrestDay(g, c, r):
    if r in g[c] or r == c:
        print(1)
    else:
        print(2)


arrestDay(city_graph, c, r)







