# [Better Approach - 2] - Using Bottom-Up DP(Tabulation) – O(n) Time and O(n) Space--------------------------------------


# def minCost(height):
#     n = len(height)
#     min_cost = [0 for _ in range(n)]
    
#     if n == 1:
#         return 0
#     if n == 2:
#         return abs(height[1]- height[0])
    
#     min_cost[1] = abs(height[1] - height[0])
    
#     for i in range(2, n):
#         min_cost[i] = min(min_cost[i - 2] + abs(height[i] - height[i - 2]),
#                           min_cost[i - 1] + abs(height[i] - height[i - 1]))

#     return min_cost[n - 1]


# heights = [20, 30, 40, 20]
# print(minCost(heights))

# [Expected Approach] - Using Space Optimized DP – O(n) Time and O(1) Space---------------------------------------
def minCost(height):
    n = len(height)

    if n == 1:
        return 0

    # Variables prev1 and prev2 to store the result
    # of last and second last states
    prev2 = 0
    prev1 = abs(height[1] - height[0])

    for i in range(2, n):
        curr = min(prev1 + abs(height[i] - height[i - 1]),
                   prev2 + abs(height[i] - height[i - 2]))

        # Updating prev2 to previous result and
        # prev1 to current result
        prev2 = prev1
        prev1 = curr

    # In the last iteration, final value
    # of curr is stored in  prev1
    return prev1


height = [20, 30, 40, 20]
print(minCost(height))
