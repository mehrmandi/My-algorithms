# def caseSort(s):
#     n = len(s)
#     marker = ["L" for _ in range(n)]
#     upper = []
#     lower = []
#     res = ""
    
    
#     for i in range(n):
#         if s[i].islower():
#             lower.append(s[i])          
#         else:
#             upper.append(s[i])
#             marker[i] = "U"
            
#     upper.sort()
#     lower.sort()
    
#     for i in range(n):
#         if marker[i] == "U":
#             char = upper.pop(0)
#             res += char
#         else:
#             char = lower.pop(0)
#             res += char
            
         
#     return res            
        
        
# s = "XWMSPQ"
# print(caseSort(s))

# [Expected Approach] Using Two Count Arrays of 26 Size - O(n) Time and O(1) Space-----------------------------------------

def case_sort(s):
    uppercase = sorted([ch for ch in s if ch.isupper()])
    lowercase = sorted([ch for ch in s if ch.islower()])

    result = []
    upper_idx = 0
    lower_idx = 0

    for ch in s:
        if ch.isupper():
            result.append(uppercase[upper_idx])
            upper_idx += 1
        else:
            result.append(lowercase[lower_idx])
            lower_idx += 1

    return ''.join(result)


# Example
s = "GEekS"
print(case_sort(s))  # Output: "EGeks"
