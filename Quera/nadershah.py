
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.dp = [0] * 100000


    def addEdge(self, u, v):
        self.adj[u].append(v)


    def dfs(self, a, v, u, parent):


        self.dp[u] = a[u - 1]

        maximum = 0

        # Traverse the tree
        for child in v[u]:

            if child == parent:
                continue
                
            self.dfs(a, v, child, u)


            maximum = max(maximum, self.dp[child])

        self.dp[u] += maximum


    def maximumValue(self, a, v, e, d, n):
        self.dfs(a, v, e, 0)
        max_diamond = []
        for i in self.adj[e]:
            max_diamond.append(self.dp[i])

        max_diamond.sort(reverse = True)

        maxDiamond = d[e - 1]
        if len(max_diamond) >= n:
            for i in range(n):
                maxDiamond += max_diamond[i]
        else:
            for i in range(len(max_diamond)):
                maxDiamond += max_diamond[i]

        return maxDiamond






if __name__  == "__main__":
    c = int(input())
    for i in range(c):
        V, I, A = [int(x) for x in input().split(" ")]
        V = V + 1
        d = [int(x) for x in input().split(" ")]
        g = Graph(V)

        for j in range(V - 2):
            s, e = [int(x) for x in input().split(" ")]
            g.addEdge(s, e)
            g.addEdge(e, s)


        print(g.maximumValue(d, g.adj, I, d, A))
