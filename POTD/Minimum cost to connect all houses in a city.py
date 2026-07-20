import heapq
import math

def manhattanDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def minCost(houses, n):
    min_heap = [(0, 0)]  # (cost, house_index), start from house 0
    visited = [False] * n  # Keep track of visited houses
    total_cost = 0
    num_edges = 0

    while num_edges < n:
        cost, house_idx = heapq.heappop(min_heap)

        if visited[house_idx]:
            continue

        visited[house_idx] = True
        total_cost += cost
        num_edges += 1

        for i in range(n):
            if not visited[i]:
                # Calculate the distance from the current house to the unvisited house
                dist = manhattanDistance(houses[house_idx], houses[i])
                heapq.heappush(min_heap, (dist, i))
                print(min_heap)

    return total_cost


n = 5
houses = [[0, 7], [0, 9], [20, 7], [30, 7], [40, 70]]
print(minCost(houses, n))
