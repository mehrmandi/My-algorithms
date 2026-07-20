def remainingBalls(color, radius):
    stack = []
    
    for i in range(len(color)):
        if stack and stack[-1] == (color[i], radius[i]):
            stack.pop()  # Remove the pair
            print("pop", i, stack)
        else:
            stack.append((color[i], radius[i]))  # Push current ball
            print("add", i, stack)
    
    return len(stack)

# Example usage:
color = [2, 2, 2, 3, 5]
radius = [3, 3, 3, 3, 5]
print(remainingBalls(color, radius))  # Output: 3