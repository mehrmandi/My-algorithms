from bisect import bisect_left, bisect_right

def transition_point(arr):
    l = bisect_left(arr, 1)
    r = bisect_right(arr, 1)

    if r == len(arr) and r == l:
        return -1
    elif r - l == len(arr):
        return 0
    else:
        return l


arr = [1, 1, 1]


print(transition_point(arr))