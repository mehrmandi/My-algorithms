import math
# def countBSTs(arr):
#     res_arr = [[0], [1], [1, 1], [2, 1, 2], [5, 2, 2, 5], [14, 5, 4, 5, 14], [42, 14, 10, 10, 14, 42],
#                [132, 42, 28, 25, 28, 42, 132]]
    
#     n = len(arr)
#     res = [0 for _ in range(n)]
    
#     elem_index = {element :index for index, element in enumerate(arr)}
    
#     arr.sort()
    
    
    
#     for i in range(n):
#         res_node = res_arr[n][i]
#         res[elem_index[arr[i]]] = res_node
        
#     return res
        

# arr = [145, 45, 25, 47, 65]
# print(countBSTs(arr))


# Precompute factorials up to 2*n

def computeFact(num):
    fact = [1] * (num + 1)
    for i in range(1, num + 1):
        fact[i] = fact[i - 1] * i
    return fact

# Compute nth Catalan number using precomputed factorials


def catalan(n, fact):
    return fact[2 * n] // (fact[n] * fact[n + 1])

# Function to count number of BSTs for each element as root


def countBSTs(arr):
    n = len(arr)
    sortedArr = sorted([(val, idx) for idx, val in enumerate(arr)])

    fact = computeFact(2 * n)

    numBsts = [0] * n

    # Compute BST count for each element as root
    for i, (val, idx) in enumerate(sortedArr):
        numBsts[idx] = catalan(i, fact) * catalan(n - i - 1, fact)

    return numBsts


if __name__ == "__main__":
    arr = [145, 45, 25, 47, 65]
    numBSTs = countBSTs(arr)

    print(*numBSTs)

