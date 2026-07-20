from typing import List


def longestSubarray(arr: List[int]) -> int:
    n = len(arr)

    nextGreater = [n] * n
    prevGreater = [-1] * n

    st = []

    # Find Next Greater Element to the Right
    for i in range(n):
        while st and arr[st[-1]] < arr[i]:
            nextGreater[st.pop()] = i
        st.append(i)

    print(nextGreater)
    # Clear stack for next pass
    st.clear()

    # Find Next Greater Element to the Left
    for i in range(n - 1, -1, -1):
        while st and arr[st[-1]] < arr[i]:
            prevGreater[st.pop()] = i
        st.append(i)
        
    print(prevGreater)

    # Find the maximum valid subarray length
    maxLength = 0
    for i in range(n):
        windowSize = nextGreater[i] - prevGreater[i] - 1
        if windowSize >= arr[i]:
            maxLength = max(maxLength, windowSize)

    return maxLength
        

arr = [4, 1, 3, 2, 6, 2, 4, 5, 7, 6, 8]
print(longestSubarray(arr))
