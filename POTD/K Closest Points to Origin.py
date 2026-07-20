# def kClosestPoint(points, k):
#     mapDic = {}
#     for i in points:
#         euqDis = i[0]**2 + i[1]**2
#         if euqDis in mapDic:
#             mapDic[euqDis].append(i)
#         else:
#             mapDic[euqDis] = [i]
#     sortedList = list(sorted(mapDic.items()))
#     result = []
#     for i in sortedList:
#         for j in range(len(i[1])):
#             result.append(i[1][j])
#
#     return result[:k]


import heapq
from typing import List


# def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
#     # Min-Heap to store (distance, point) tuples
#     heap = []

#     for (x, y) in points:
#         dist = x * x + y * y  # Squared Euclidean distance
#         heapq.heappush(heap, (dist, [x, y]))  # Push (distance, point) into min-heap

#     print(heap)

#     # Extract k closest points
#     return [heapq.heappop(heap)[1] for _ in range(k)]


# k = 9
# points = [[-3, 2], [9, 7], [8, 4], [6, 0], [7, -6], [2, 5], [4, 3], [0, 2], [6, 0], [9, -2]]

# print(kClosest(points, k))

import heapq

# Function to calculate squared distance from the origin


def squaredDis(point):
    return point[0] * point[0] + point[1] * point[1]

# Function to find k closest points to
# the origin


def kClosest(points, k):

    # Max heap to store points with their
    # squared distances
    maxHeap = []

    # Iterate through each point
    for i in range(len(points)):
        dist = squaredDis(points[i])

        if len(maxHeap) < k:

            # If the heap size is less than k,
            # insert the point
            heapq.heappush(maxHeap, (-dist, points[i]))
        else:

            # If the heap size is k, compare with
            # the top element
            if dist < -maxHeap[0][0]:

                # Replace the top element if the
                # current point is closer
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (-dist, points[i]))

    # Take the k closest points from the heap
    res = []
    while maxHeap:
        res.append(heapq.heappop(maxHeap)[1])

    return res


if __name__ == "__main__":
    points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
    k = 2

    res = kClosest(points, k)

    for point in res:
        print(f"{point[0]}, {point[1]}")
