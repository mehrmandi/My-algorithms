# def asciiRangeSum(s):
#     n = len(s)
#     hash_pre = {-1: 0}
#     hash_asc = {}
#     res = {}
#     res_arr = []
#     prefix_sum = 0
    
#     for i in range(n):
#         asc = ord(s[i])
#         prefix_sum += asc
#         hash_pre[i] = prefix_sum
#         if asc in hash_asc:
#             pre_loc = hash_asc[asc]
#             dot_sum = hash_pre[i] - hash_pre[pre_loc] - asc
#             hash_asc[asc] = i
#             if asc not in res:
#                 res[asc] = dot_sum
#             else:
#                 res[asc] = res[asc] + dot_sum + asc
            
#         if asc not in hash_asc:
#             hash_asc[asc] = i
            
#     for key, val in res.items():
#         if val > 0:
#             res_arr.append(val)
        
#     return res_arr
    
            
# s = "acdacabbcdanb"
# print(asciiRangeSum(s))

#[Expected Approach] Space-Optimized Range Sum Using First and Last Indices - O(n) Time and O(1) Space

def asciirange(s):
    result = []
    n = len(s)

    # Initialize all indices to -1
    first = [-1] * 26
    last = [-1] * 26

    # Track first and last
    # occurrence of each character
    for i in range(n):
        idx = ord(s[i]) - ord('a')
        if first[idx] == -1:
            first[idx] = i
        else:
            last[idx] = i

    # Compute ASCII sums
    # between first and last occurrence
    for i in range(26):
        if first[i] != -1 and last[i] != -1:
            sumval = 0
            for j in range(first[i] + 1, last[i]):
                sumval += ord(s[j])
            if sumval != 0:
                result.append(sumval)

    # Sort the results in increasing order

    return result


if __name__ == "__main__":
    s = "acdacabbcdanb"

    result = asciirange(s)

    for val in result:
        if val != 0:
            print(val, end=' ')
