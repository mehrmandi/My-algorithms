def can_achieve(arr, k, w, target):
    n = len(arr)
    ops = [0] * (n + w + 1)
    total_ops = 0
    water = 0

    for i in range(n):
        water += ops[i]
        current_height = arr[i] + water
        if current_height < target:
            need = target - current_height
            if total_ops + need > k:
                return False
            total_ops += need
            water += need
            ops[i + w] -= need  # rollback after w range

    return True


def maximize_min_height(arr, k, w):
    low = min(arr)
    high = max(arr) + k
    answer = low

    while low <= high:
        mid = (low + high) // 2
        if can_achieve(arr, k, w, mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer
        
arr = [2, 3, 4, 5, 1]
k = 2
w = 2
print(maximize_min_height(arr, k, w))
