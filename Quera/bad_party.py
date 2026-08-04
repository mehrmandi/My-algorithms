def guste():
    n = int(input())

    size = 300000

    edges = []

    parent = [i for i in range(size)]

    rep = []

    final_rep = []

    for i in range(n):
        person = [int(x) for x in input().split(" ")]
        edges.append(person)

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent_x = find(x)
        parent_y = find(y)
        if parent_x != parent_y:
            parent[parent_y] = parent_x

        rep.append(parent_x)

    for x, y in edges:
        union(x, y)

    for val in rep:
        final_rep.append(find(val))

    guest = len(set(final_rep)) - 1

    print(guest)


guste()