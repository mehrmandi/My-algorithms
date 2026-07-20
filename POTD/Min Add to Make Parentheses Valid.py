def minParentheses(s):
    n = len(s)
    res = 0
    i = 0
    couple_par = 0
    
    for i in range(n):
        if couple_par == 0:
            if s[i] == ')':
                res += 1
            else:
                couple_par += 1
        else:
            if s[i] == ')':
                couple_par -= 1
            else:
                couple_par += 1
    
    res += abs(couple_par)
    
    return res
    

s = ")))"

print(minParentheses(s))
