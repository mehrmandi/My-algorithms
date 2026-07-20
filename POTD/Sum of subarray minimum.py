# def sumSubMins(arr):
#     n = len(arr)
#     dp = [0] * n
#     right = [i for i in range(n)]
#     stack = []

#     # Find index of next
#     # smaller element on the right
#     for i in range(n):
#         while stack and arr[i] < arr[stack[-1]]:
#             right[stack.pop()] = i
#         stack.append(i)
        
#     print(right)

#     # Fill dp[] from right to left
#     dp[n - 1] = arr[n - 1]
#     for i in range(n - 2, -1, -1):
#         r = right[i]
#         if r == i:
#             dp[i] = (n - i) * arr[i]
#         else:
#             dp[i] = (r - i) * arr[i] + dp[r]
    
#     return sum(dp)


# if __name__ == "__main__":
#     arr = [3, 1, 2, 4, 2, 7, 3]
#     print(sumSubMins(arr))
    
    
    
def sumSubMins(arr):
        # Code here
        stack = []
        
        
        n = len(arr)
        prev = [None] * n
        next_ = [None] * n
    
        # Previous Less Element (Strictly less)
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
    
        stack.clear()
    
        # Next Less Element (Less than or equal)
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_[i] = stack[-1] if stack else n
            stack.append(i)
            
        print(prev, next_)
    
        # Sum contributions
        total = 0
        for i in range(n):
            left = i - prev[i]
            right = next_[i] - i
            total += arr[i] * left * right
        return total


if __name__ == "__main__":
    arr = [3, 1, 2, 4, 2, 7, 3]
    print(sumSubMins(arr))
        


