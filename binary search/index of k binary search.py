
# Python program for the above approach

# Function to find insert position of K
def find_index(arr, n, K):
    index = float('inf')

    for i in range(n):

        if arr[i] == K:
            if i < index:
                index = i


    if index <= n:
        return index
    return -1


# Driver Code
arr = [11, 22, 33, 44, 55]
n = len(arr)
K = 1
print(find_index(arr, n, K))