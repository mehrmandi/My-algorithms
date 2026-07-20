def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    print(left, right)
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # ادغام دو لیست مرتب‌شده
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            print("left", left[i], right[j])
            result.append(left[i])
            i += 1
        else:
            print("right", left[i], right[j])
            result.append(right[j])
            j += 1
        print("result", result)
    # اضافه‌کردن باقی‌مانده‌ها
    result.extend(left[i:])
    result.extend(right[j:])
    print("final", result)
    return result


# تست
arr = [5, 2, 9, 1]
print(merge_sort(arr))  # خروجی: [1, 2, 5, 9]
