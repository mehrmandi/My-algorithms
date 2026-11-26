# Given a string s and a 2D array queries[][], where each query consists of two integers l and r, find the number of vowels in the substring s[l....r] for each query. The substring includes both indices l and r.

# Return an array containing the answers to all queries in the order they are given.


# Prefix Sum - O(n + q) Time and O(n) Space

def countVowels(s: str, queries: list[list[int]]) -> list[int]:
    n = len(s)
    vowels_count = [0] * (n + 1)
    vowels = ["o", "u", "a", "e", "i"]
    res = []
    
    
    for i in range(1, n + 1):
        if s[i - 1] in vowels:
            vowels_count[i] = vowels_count[i - 1] + 1
            
        else:
            vowels_count[i] = vowels_count[i - 1]
            
    for q in queries:
        s , e = q[0], q[1] + 1
        
        res.append(vowels_count[e] - vowels_count[s])
        
        
    return res
        

s = "helloworld"
queries = [[0, 4], [5, 9], [0, 9]]
print(countVowels(s, queries))
