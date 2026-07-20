from collections import defaultdict


# Function to find Majority element in a list
# It returns -1 if there is no majority element
def majority_element(arr):
    n = len(arr)
    count_map = defaultdict(int)

    # Traverse the list and count occurrences using the hash map
    for num in arr:
        count_map[num] += 1

        # Check if current element count exceeds n / 2
        if count_map[num] > n / 2:
            return num

    # If no majority eleme
    return -1


arr = [1, 2, 2, 2, 2, 2, 2, 2, 3, 4, 4, 5, 5]
print(majority_element(arr))
