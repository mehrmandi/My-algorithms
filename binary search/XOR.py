def find_missing_numbers(arr, n):
    XOR = 0

    # XORing [1..n] with the elements present in the array
    # cancels the identical numbers. So at the end, we will
    # get the missing number.
    for i in range(n - 1):
        print(XOR, arr[i])
        XOR ^= arr[i]
        print("first", XOR)

    for i in range(1, n + 1):
        print("second", XOR, i)
        XOR ^= i
        print("sec", XOR)

    return XOR


# Driver code
if __name__ == "__main__":
    arr = [1, 2, 4, 5]
    n = 5
    print(find_missing_numbers(arr, n))