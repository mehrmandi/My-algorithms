def factorial(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return n * factorial(n - 1)
    
def vowelCount(s):
    hash = {}
    vowel = ["a", "e", "i", "u", "o"]
    
    for char in s:
        if char in vowel:
            hash[char] = hash.get(char, 0) + 1
    
    dist = len(hash)
    res = factorial(dist)
    
    for key, val in hash.items():
        if val > 1:
            res *= val
            
    return res


s = "k"
print(vowelCount(s))

