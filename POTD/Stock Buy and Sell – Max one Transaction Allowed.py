def maxProfit(prices):
    n = len(prices)
    stk = [prices[0]]
    res = 0
    
    for i in range(1, n):
        while stk  and prices[i] < stk[-1]:
            stk.pop()
        
        if stk and prices[i] > stk[-1]:
            res = max(res, prices[i] - stk[-1])
        
        else:
            stk.append(prices[i])
        
    return res


# [Expected Approach] One Traversal Solution - O(n) Time and O(1) Space-------------
def maxProfit(prices):
    minSoFar = prices[0]
    res = 0

    for i in range(1, len(prices)):

        # Update the minimum value seen so far
        minSoFar = min(minSoFar, prices[i])

        # Update result if we get more profit
        res = max(res, prices[i] - minSoFar)

    return res
    
    
prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))
