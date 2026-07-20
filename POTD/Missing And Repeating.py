
# [Expected Approach] Negative Marking approach - O(n) Time and O(1) Space-----------

def findTwoElement(arr):
    normal = 0
    sum_arr = 0
    ans = []

    for i in range(len(arr)):
        normal += i + 1
        sum_arr += abs(arr[i])

        # convert value to index (1-based to 0-based)
        idx = abs(arr[i]) - 1

        # if already visited, it's a duplicate
        if arr[idx] < 0:
            ans.append(abs(arr[i]))
        else:

            # mark as visited
            arr[idx] = -arr[idx]
            
    missing_num = normal - sum_arr + ans[0]
    ans.append(missing_num)
    return ans


arr = [2, 2]
print(findTwoElement(arr))
