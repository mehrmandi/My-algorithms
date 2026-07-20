# Time Complexity: O(N*K)
# Space Complexity: O(N*K)


class Solution:

    def minCost(self, costs) -> int:
        n = len(costs)
        m = len(costs[0])

        # 1 color + multiple walls - impossible
        if m == 1 and n > 1:
            return -1

        # Track smallest, second smallest, and index of smallest in previous row
        prevMin1 = float('inf')
        prevMin2 = float('inf')
        minIndex = -1

        # First row: find min1, min2
        for j in range(m):
            val = costs[0][j]
            if val < prevMin1:
                prevMin2 = prevMin1
                prevMin1 = val
                minIndex = j
            elif val < prevMin2:
                prevMin2 = val

        # Process next rows
        for i in range(1, n):

            currMin1 = float('inf')
            currMin2 = float('inf')
            currIndex = -1

            for j in range(m):

                # Can't use prevMin1 if same color as previous row
                cost = costs[i][j] + (prevMin2 if j == minIndex else prevMin1)

                # Update min1, min2 for this row
                if cost < currMin1:
                    currMin2 = currMin1
                    currMin1 = cost
                    currIndex = j
                elif cost < currMin2:
                    currMin2 = cost

            # Move current -> previous
            prevMin1 = currMin1
            prevMin2 = currMin2
            minIndex = currIndex

        return prevMin1
