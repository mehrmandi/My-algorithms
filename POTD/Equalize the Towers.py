# 


# def minCostToEqualHeight(heights, cost):
#     def total_cost(target_height):
#         return sum(abs(h - target_height) * c for h, c in zip(heights, cost))

#     # Binary search between the minimum and maximum possible height
#     low, high = min(heights), max(heights)
#     result = float('inf')

#     while low < high:
#         mid1 = low + (high - low) // 3
#         mid2 = high - (high - low) // 3

#         cost1 = total_cost(mid1)
#         cost2 = total_cost(mid2)

#         result = min(result, cost1, cost2)

#         if cost1 < cost2:
#             high = mid2 - 1
#         else:
#             low = mid1 + 1

#     # Check final range to ensure minimum cost is captured
#     for h in range(low - 2, high + 3):
#         result = min(result, total_cost(h))

#     return result


# Weighted Median O(n log n)--------------------------------------

def minCost(heights, cost):
    # code her
    towers = sorted(zip(heights, cost))
    

    total_weight = sum(cost)
    cumulative_weight = 0

       # Step 2: Find weighted median
    for h, c in towers:
        cumulative_weight += c
        if cumulative_weight >= total_weight / 2:
            target = h
            break

        # Step 3: Compute minimum cost
    return sum(abs(h - target) * c for h, c in towers)
# Example usage:
heights = [1, 5, 3, 6, 8]
cost = [10, 7, 9, 11, 4]
print(minCost(heights, cost))  # Output: 120







