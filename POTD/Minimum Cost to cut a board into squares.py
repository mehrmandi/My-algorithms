# import heapq

# def minCost(n, m, x, y):
#     hor_seg = 1
#     ver_seg = 1
#     cost = 0
#     max_heap = []
    
    
#     for i in range(n - 1):
#         heapq.heappush(max_heap, (-y[i], "y"))
        
#     for j in range(m - 1):
#         heapq.heappush(max_heap, (-x[j], "x"))
        
    
#     while max_heap:
#         val, axis = heapq.heappop(max_heap)
        
#         if axis == "y":
#             cost += -val * ver_seg
#             hor_seg += 1
            
#         if axis == "x":
#             cost += -val * hor_seg
#             ver_seg += 1
            
#     return cost
    

# n = 4
# m = 4
# x = [1, 1, 1]
# y = [1, 1, 1]
# print(minCost(n, m, x, y))


def minCost(n, m, x, y):

    # Sort the cutting costs in ascending order
    x.sort()
    y.sort()

    hCount, vCount = 1, 1
    i, j = len(x) - 1, len(y) - 1
    totalCost = 0
    while i >= 0 and j >= 0:

        # Choose the larger cost cut to
        # minimize future costs
        if x[i] >= y[j]:
            totalCost += x[i] * hCount
            vCount += 1
            i -= 1
        else:
            totalCost += y[j] * vCount
            hCount += 1
            j -= 1

    # Process remaining vertical cuts
    while i >= 0:
        totalCost += x[i] * hCount
        vCount += 1
        i -= 1

    # Process remaining horizontal cuts
    while j >= 0:
        totalCost += y[j] * vCount
        hCount += 1
        j -= 1

    return totalCost


if __name__ == "__main__":

    n, m = 4, 4
    x = [1, 1, 1]
    y = [1, 1, 1]

    print(minCost(n, m,x, y))