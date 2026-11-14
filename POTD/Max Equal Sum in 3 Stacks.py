# Given three stacks s1, s2, and s3, represented by arrays where the first element of each array represents the top of the corresponding stack.

# Find the maximum possible equal sum(sum of all elements) of all three stacks by removing zero or more elements from the top of each stack.

# If it is not possible to make the sum of all three stacks equal, return 0.

# Greedy Approach - O(n1 + n2 + n3) Time and O(1) Space


def maxEqualSum(s1: list[int], s2: list[int], s3: list[int]) -> int:
    sum1 = sum(s1)
    sum2 = sum(s2)
    sum3 = sum(s3)
    
    n1 = len(s1)
    n2 = len(s2)
    n3 = len(s3)
    
    f1 = 0
    f2 = 0
    f3 = 0

    while f1 < n1 and f2 < n2 and f3 < n3:
        if sum1 == sum2 == sum3:
            return sum1

        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= s1[f1]
            f1 += 1
            
        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= s2[f2]
            f2 += 1
        else:
            sum3 -= s3[f3]
            f3 += 1
            
    return 0

s1 = [4, 7]
s2 = [10]
s3 = [1, 2, 3]
print(maxEqualSum(s1, s2, s3))