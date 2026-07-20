import sys
import heapq

INF = 10**30


def solve():
    n, m = map(int, input().split())
    price = list(map(int, input().split()))

    graph = [[] for _ in range(n)]
    for _ in range(m):
        v, u, w = map(int, input().split())
        v -= 1
        u -= 1
        graph[v].append((u, w))
        graph[u].append((v, w))
    ans = [[INF]*n for _ in range(n)]

    for s in range(n):
        dist = [[INF]*n for _ in range(n)]
        dist[s][s] = 0
        pq = [(0, s, s)]  # cost, node, cheapest_city

        while pq:
            cost, v, k = heapq.heappop(pq)
            print("pq", cost, v, k, dist[v][k], graph[v])
            if cost != dist[v][k]:
                continue

            for u, w in graph[v]:
                nk = k if price[k] <= price[u] else u
                ncost = cost + w * price[k]
                if ncost < dist[u][nk]:
                    dist[u][nk] = ncost
                    heapq.heappush(pq, (ncost, u, nk))

        for t in range(n):
            ans[s][t] = min(dist[t])

    return ans


# INF = 10**30
# input = sys.stdin.readline


# def solve():
#     n, m = map(int, input().split())
#     price = list(map(int, input().split()))

#     graph = [[] for _ in range(n)]
#     for _ in range(m):
#         v, u, w = map(int, input().split())
#         v -= 1
#         u -= 1
#         graph[v].append((u, w))
#         graph[u].append((v, w))
    

#     ans = [[INF]*n for _ in range(n)]

#     for s in range(n):
#         dist = [[INF]*n for _ in range(n)]
#         dist[s][s] = 0

#         pq = [(0, s, s)]  # cost, current_city, cheapest_city

#         while pq:
#             cost, v, k = heapq.heappop(pq)
#             if cost != dist[v][k]:
#                 continue

#             # اگر برای شهر v پاسخ نهایی بهتر پیدا شده، ادامه نده
#             if cost >= ans[s][v]:
#                 continue

#             ans[s][v] = min(ans[s][v], cost)

#             for u, w in graph[v]:
#                 # cheapest city update
#                 if price[u] < price[k]:
#                     nk = u
#                 else:
#                     nk = k

#                 ncost = cost + w * price[k]
#                 if ncost < dist[u][nk]:
#                     dist[u][nk] = ncost
#                     heapq.heappush(pq, (ncost, u, nk))

#     # output
#     for i in range(n):
#         print(*ans[i])


if __name__ == "__main__":
    print(solve())
