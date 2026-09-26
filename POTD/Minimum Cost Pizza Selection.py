# Given the area of Small, Medium, and Large pizzas as s, m, and l units, and their respective costs as cs, cm, and cl, find the minimum amount of money required to buy pizzas whose total area is at least x. You may buy any number of pizzas of each type.

# Dynamic Programming - O(x) Time and O(x) Auxiliary Space
def minimumCost(x, s, m, l, cs, cm, cl):
    # create a dynamic programming array to store the minimum cost for each area up to x + l
    limit = x + l
    dp = [float('inf')] * (limit + 1)
    dp[0] = 0
    pieces = [s, m, l]
    costs = [cs, cm, cl]
    
    for i in range(3):
        # Update the dp array for each pizza type
        for c in range(pieces[i], limit + 1):
            dp[c] = min(dp[c] ,  dp[c - pieces[i]] + costs[i])
    
    # After filling the dp array, find the minimum cost for any area from x to limit        
    for c in range(x, limit + 1):
        dp[x] = min(dp[x], dp[c])
                               
    return dp[x]

            

x = 41
s = 8
m = 8
l = 8
cs = 16
cm = 19
cl = 19
print(minimumCost(x, s, m, l, cs, cm, cl))
