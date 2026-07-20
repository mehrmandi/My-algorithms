# def prefixSum2D(mat, queries):
#     q = len(queries)
    
#     res = [0 for _ in range(q)]
    
#     for i in range(q):
#         queries[i].append(i)
        
    
#     while queries:
#         rs, cs, re, ce, idx = queries.pop()
        
#         res[idx] += sum(mat[rs][cs:ce + 1])
        
#         if rs < re :
#             queries.append([rs + 1, cs, re, ce, idx])
            
#     return res
# Time Complexity: O(n × m + q), where n is the number of rows, m is the number of columns, and q is the number of queries. Each query is handled in O(1) time.
# Auxiliary Space: O(n × m + q), where n is the number of rows, m is the number of columns(for storing the prefix sum matrix), and q is the number of queries(for storing the results).


mat = [[1, 2, 3], 
        [1, 1, 0],
        [4, 2, 2]]

queries = [[0, 0, 1, 1], [1, 0, 2, 2]]


def sumQuery(aux, tli, tlj, rbi, rbj):

    # result is now sum of elements
    # between (0, 0) and (rbi, rbj)
    res = aux[rbi][rbj]

    # Remove elements between (0, 0)
    # and (tli-1, rbj)
    if (tli > 0):
        res = res - aux[tli - 1][rbj]

    # Remove elements between (0, 0)
    # and (rbi, tlj-1)
    if (tlj > 0):
        res = res - aux[rbi][tlj - 1]

    # Add aux[tli-1][tlj-1] as elements
    # between (0, 0) and (tli-1, tlj-1)
    # are subtracted twice
    if (tli > 0 and tlj > 0):
        res = res + aux[tli - 1][tlj - 1]

    return res

def prefixSum2D(mat, queries):
    M = len(mat)
    N = len(mat[0])
    
    aux = [[0 for _ in range(N)] for _ in range(M)]
    
    res = []
   
    for i in range(0, N):
        aux[0][i] = mat[0][i]

    # Do column wise sum
    for i in range(1, M):
        for j in range(0, N):
            aux[i][j] = mat[i][j] + aux[i - 1][j]

    # Do row wise sum
    for i in range(0, M):
        for j in range(1, N):
            aux[i][j] += aux[i][j - 1]
            
            
    for q in queries:
        tli, tlj, rbi, rbj = q
        res.append(sumQuery(aux, tli, tlj, rbi, rbj))
        
    return res
    

print(prefixSum2D(mat, queries))
    
