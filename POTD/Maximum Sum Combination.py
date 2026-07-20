import heapq


def k_max_combinations(a, b, k):
    a.sort(reverse=True)
    b.sort(reverse=True)
    n = len(a)

    max_heap = []
    visited = set()

    # Start with the largest possible sum
    heapq.heappush(max_heap, (-(a[0] + b[0]), 0, 0))
    visited.add((0, 0))

    result = []
    while len(result) < k and max_heap:
        current_sum, i, j = heapq.heappop(max_heap)
        result.append(-current_sum)

        if i + 1 < n and (i + 1, j) not in visited:
            heapq.heappush(max_heap, (-(a[i + 1] + b[j]), i + 1, j))
            visited.add((i + 1, j))

        if j + 1 < n and (i, j + 1) not in visited:
            heapq.heappush(max_heap, (-(a[i] + b[j + 1]), i, j + 1))
            visited.add((i, j + 1))

    return result
