# Time complexity: O(n2) because in the worst case each stone can lie in a unique component, and therefore we make dfs call for each stone, each dfs call takes O(n) because we check if any stone shares the same row or column as current stone.
# Auxiliary Space: O(n) for recursive stack and visited array.



def dfs(i, visited, stones):
    if visited[i]:
        return
    visited[i] = True

    for j in range(len(stones)):

        # if another stone has same row or
        # column as this stone then both lie
        # in the same component
        if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
            dfs(j, visited, stones)


def maxRemove(stones):
    n = len(stones)

    visited = [False] * n
    components = 0

    for i in range(n):

        # visiting the stone if not visited
        # and finding all the stones lying in
        # the same component as this stone
        if not visited[i]:
            dfs(i, visited, stones)
            components += 1

    # atleast 1 stone per component
    # cannot be removed
    return n - components




stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
print(maxRemove(stones))


# Time complexity: O(n2 + n log n), n2 is because we check for each pair of stone if they are in the same row or column, n log n because for all stones, we call the findParent function that takes O(log n) time.
# Auxiliary Space: O(n) for parent and rank array.

# find parent of the component a stone lies in
# def findParent(i, par):
#     if par[i] == i:
#         return i
#     par[i] = findParent(par[i], par)
#     return par[i]


# merging components based on ranks

# def union(u, v, par, rank):
#     pu = findParent(u, par)
#     pv = findParent(v, par)

#     # if both lie in same component, return
#     if pu == pv:
#         return

#     # merging components based on ranks
#     if rank[pu] == rank[pv]:
#         par[pu] = pv
#         rank[pv] += 1
#     elif rank[pu] > rank[pv]:
#         par[pv] = pu
#     else:
#         par[pu] = pv


# def maxRemove(stones):
#     n = len(stones)

#     # parent denotes the parent node
#     # of the component a stone lies in
#     par = list(range(n))
#     rank = [0] * n

#     # initially each stone is in a different component
#     for i in range(n):
#         par[i] = i

#     # for each pair of stones, we check if
#     # they are in the same row or column
#     for i in range(n):
#         for j in range(i + 1, n):

#             # to check for same row or column
#             if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
#                 union(i, j, par, rank)

#     components = set(findParent(i, par) for i in range(n))

#     return n - len(components)


# if __name__ == "__main__":
#     stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]

#     print(maxRemove(stones))
