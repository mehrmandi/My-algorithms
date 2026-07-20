def is_subset_using_hashing(arr1, arr2):

    # Create a hash set and insert all elements of arr1
    hash_set = set(arr1)

    # Check each element of arr2 in the hash set
    for num in arr2:
        if num not in hash_set:
            return False

    # If all elements of arr2 are found in the hash set
    return True


# Driver code
arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 7, 1]

if is_subset_using_hashing(arr1, arr2):
    print("Yes")
else:
    print("No")


    # for i in range(n):
    #     found = False
    #
    #     # Check if the element exists in the first array
    #     for j in range(m):
    #         if arr2[i] == arr1[j]:
    #             found = True
    #             break
    #
    #     # If any element is not found, return false
    #     if not found:
    #         return False
    #
    # # If all elements are found, return true
    # return True