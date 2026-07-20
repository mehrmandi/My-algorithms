def extra_element_index(a, b):
    extra_elem = sum(a) - sum(b)

    nB = len(b)

    low = 0
    high = nB - 1

    if extra_elem < b[low]:
        return 0

    elif extra_elem > b[high]:
        return nB

    else:

        while low < high - 1:
            mid = low + (high - low) // 2

            if b[low] < extra_elem < b[mid]:
                high = mid

            else:
                low = mid

        return low + 1





a = [3,5,7,8,11,13]
b = [3,5,7,11,13]

print(extra_element_index(a, b))